# Next.js SaaS Starter, Reference

Canonical reference for the official Vercel SaaS starter at https://github.com/nextjs/saas-starter. Use this when Timo or any project references this template, scaffolds from it, or asks "how does the Next SaaS starter do X".

- Repo: `nextjs/saas-starter` (MIT, 15.8k+ stars, primary lang TypeScript)
- Live demo: https://next-saas-start.vercel.app
- Default branch: `main`. Last meaningful push tracked 2025-12-11.

## What it is
A minimal, production-shaped SaaS starter with auth, teams, Stripe billing, and a dashboard. Designed as a learning resource, not a kitchen-sink template. Paid alternatives the README itself lists: Achromatic, ShipFast, MakerKit, Zero to Shipped, TurboStarter.

## Tech stack
- **Next.js 15.6 canary** (App Router, Server Actions, `--turbopack` dev)
- **React 19.1**
- **PostgreSQL** + **Drizzle ORM 0.43** + **drizzle-kit 0.31**
- **Stripe** (`stripe@18`, API version `2025-04-30.basil`). Checkout + Customer Portal + Webhooks
- **shadcn/ui** (Radix UI primitives, `lucide-react`, `class-variance-authority`, `tailwind-merge`)
- **Tailwind CSS v4** + `@tailwindcss/postcss` + `tw-animate-css`
- **Auth**: `bcryptjs` + `jose` (JWT in httpOnly cookie). No NextAuth/Clerk.
- **Validation**: `zod`
- **Data fetching**: `swr`
- **pnpm** is the package manager

## Repo layout (every file)
```
.env.example
drizzle.config.ts
middleware.ts                       <- global auth gate, refreshes session cookie on GET
next.config.ts
package.json / pnpm-lock.yaml
postcss.config.mjs
tsconfig.json
components.json                     <- shadcn config

app/
  layout.tsx
  globals.css
  not-found.tsx
  favicon.ico
  (dashboard)/                      <- route group: marketing + app shell
    layout.tsx
    page.tsx                        <- landing
    terminal.tsx                    <- animated hero terminal
    pricing/
      page.tsx
      submit-button.tsx
    dashboard/
      layout.tsx
      page.tsx
      general/page.tsx
      security/page.tsx
      activity/page.tsx
      activity/loading.tsx
  (login)/
    actions.ts                      <- ALL auth + team server actions
    login.tsx                       <- shared sign-in/up form
    sign-in/page.tsx
    sign-up/page.tsx
  api/
    stripe/checkout/route.ts        <- success redirect, sets session
    stripe/webhook/route.ts         <- subscription.updated/deleted
    team/route.ts                   <- SWR endpoint
    user/route.ts                   <- SWR endpoint

components/ui/                      <- avatar, button, card, dropdown-menu, input, label, radio-group

lib/
  utils.ts                          <- cn() helper
  auth/
    session.ts                      <- hashPassword, signToken, getSession, setSession
    middleware.ts                   <- validatedAction, validatedActionWithUser, withTeam HOFs
  db/
    drizzle.ts                      <- postgres-js client + db
    schema.ts                       <- users, teams, teamMembers, activityLogs, invitations
    queries.ts                      <- getUser, getTeamForUser, getActivityLogs, etc.
    seed.ts
    setup.ts                        <- interactive .env bootstrapper
    migrations/0000_soft_the_anarchist.sql + meta/
  payments/
    stripe.ts                       <- checkout, portal, price/product fetchers, sub sync
    actions.ts                      <- checkoutAction, customerPortalAction (withTeam HOF)
```

## Scripts
```
pnpm dev          next dev --turbopack
pnpm build        next build
pnpm start        next start
pnpm db:setup     tsx lib/db/setup.ts        (interactive: writes .env)
pnpm db:seed      tsx lib/db/seed.ts         (creates test@test.com / admin123)
pnpm db:generate  drizzle-kit generate
pnpm db:migrate   drizzle-kit migrate
pnpm db:studio    drizzle-kit studio
```

## Environment variables (.env)
- `BASE_URL`
- `POSTGRES_URL`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `AUTH_SECRET` (JWT signing key. `setup.ts` generates 32 random bytes)

## Local bootstrap flow
1. `git clone ... && pnpm install`
2. `pnpm db:setup`. Interactive: checks Stripe CLI auth, asks local-Docker-Postgres vs remote (local spins a `postgres:16.4` Docker container on port `54322` via generated `docker-compose.yml`), prompts for `STRIPE_SECRET_KEY`, runs `stripe listen --print-secret` to get the webhook secret, generates `AUTH_SECRET`, writes `.env`.
3. `pnpm db:migrate && pnpm db:seed`
4. `stripe login && stripe listen --forward-to localhost:3000/api/stripe/webhook`
5. `pnpm dev`. Test card `4242 4242 4242 4242`, any future expiry, any CVC.

## Architectural patterns to remember

### Auth = JWT in httpOnly cookie, refreshed by middleware
- `lib/auth/session.ts`. `signToken`/`verifyToken` use `jose` (HS256, 1d). `setSession` writes `session` cookie (`httpOnly`, `secure`, `sameSite: lax`).
- `middleware.ts` protects `/dashboard/*`. On every GET with a valid session, it re-signs the token to slide the 1-day expiry forward. On verify failure, it deletes the cookie and redirects protected routes to `/sign-in`. Matcher excludes `api`, `_next/*`, `favicon.ico`. Runtime is **`nodejs`** (required because `bcryptjs` is used in actions, but middleware itself only verifies JWT).
- No NextAuth, no OAuth, no email magic links. Email/password only.

### Server Actions are the API
The login flow, account management, team management, and Stripe checkout are all Server Actions in `app/(login)/actions.ts` and `lib/payments/actions.ts`. The `/api/*` routes only exist for things that genuinely need to be HTTP endpoints (Stripe webhook, SWR fetch endpoints, Stripe success redirect).

### Action wrappers (the key idiomatic pattern)
`lib/auth/middleware.ts` exports three higher-order functions used everywhere:
- `validatedAction(zodSchema, fn)`. Parses FormData with Zod, returns `{ error }` on failure.
- `validatedActionWithUser(zodSchema, fn)`. Same plus injects authed `User`, throws if not signed in.
- `withTeam(fn)`. Injects `TeamDataWithMembers`, redirects to `/sign-in` if no user.

Pattern: every Server Action is a `validated*` or `withTeam` wrapped function. Don't write raw server actions, wrap them.

### Database schema (multi-tenant via teams)
- `users`: id, name, email, passwordHash, role, soft-delete `deletedAt`.
- `teams`: id, name, plus Stripe fields: `stripeCustomerId`, `stripeSubscriptionId`, `stripeProductId`, `planName`, `subscriptionStatus`.
- `teamMembers`: junction with per-team `role` (Owner/Member). RBAC lives here, not on `users`.
- `activityLogs`: userId, teamId, action (enum: `SIGN_UP`, `SIGN_IN`, `UPDATE_PASSWORD`, `CREATE_TEAM`, `INVITE_MEMBER`, etc.), ipAddress, timestamp.
- `invitations`: pending email invites with role + status. **Email sending is a TODO**. Code has a literal TODO comment about sending invitation email and including `?inviteId={id}` in the sign-up URL. You have to wire your own SMTP/Resend.
- Exported types: `User`, `Team`, `NewUser`, etc., plus `TeamDataWithMembers` (team + members + user details) and `ActivityType` enum.

### Stripe integration
- `createCheckoutSession({ team, priceId })`. Creates Stripe Checkout in `subscription` mode with **14-day trial**, redirects unauth users to sign-up, success URL hits `/api/stripe/checkout` to set the session.
- `createCustomerPortalSession(team)`. Creates a portal config that allows: subscription update with proration, payment method changes, cancellation with reason collection.
- `handleSubscriptionChange(subscription)`. Webhook handler for `customer.subscription.updated` and `customer.subscription.deleted`. Looks up team by `stripeCustomerId`, calls `updateTeamSubscription()` to sync `subscriptionStatus`, `planName`, `stripeProductId`, `stripeSubscriptionId`. Other event types are logged but ignored (returns 200 to keep webhook delivery healthy).
- `getStripePrices()` / `getStripeProducts()`. Read-side helpers used by `/pricing`.

### Production deploy
Vercel-first. Steps: push to GitHub, import to Vercel, set env vars, in Stripe Dashboard create a webhook pointing at `https://yourdomain/api/stripe/webhook` listening for `customer.subscription.*` events, copy that signing secret into Vercel as `STRIPE_WEBHOOK_SECRET`.

## Things this starter intentionally doesn't have
- No email sending (invites are TODO).
- No OAuth / social login.
- No 2FA.
- No file uploads / blob storage.
- No background jobs / queues.
- No tests.
- No i18n.
- No multi-tenancy beyond the team table (no per-tenant schemas).
- No analytics / posthog wiring.

## When to recommend it vs alternatives
Recommend the starter when: the user wants to learn the patterns, wants minimal lock-in, is happy to wire email + extras themselves, and values a small surface area. Recommend a paid template (Achromatic / Makerkit / etc.) when they need email, OAuth, multi-org with invites, marketing site CMS, and don't want to build that scaffolding.

## Verify-before-recommend
This file is a snapshot. The repo last pushed 2025-12-11. Today is 2026-05-07. Before quoting an exact filename or API version, re-fetch the file via `gh api` or `WebFetch` of the raw URL and confirm. The `next` version (`15.6.0-canary.59`) and Stripe API version (`2025-04-30.basil`) are especially likely to drift.
