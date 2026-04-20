# Mining Angles Library

Each angle is a LENS for re-reading raw transcripts. Different angles surface different quotes from the same source. This is why raw files must be immutable: each fresh mining pass can pull new gold the prior passes missed.

## Default extraction angles (used by `/coaching-db extract`)

The first-pass extraction should cover these angles at minimum:

- `before-state` - What life was like before the solution. Pre-purchase pain.
- `transformation` - What changed. Before/after with specifics.
- `specific-result` - Named outcome with numbers, timeframes, or unique proof.
- `why-harrison` - What differentiated the coach/program from alternatives.
- `what-they-tried` - Failed methods. Prior attempts. "I did X and Y and Z."
- `recommendation` - Endorsement language. Testimonial-style.
- `identity` - Who they became. Shift from old self to new self.

## Re-mining angles (used by `/coaching-db mine <angle>`)

Each of these is an orthogonal lens. Run any of them against the existing raw corpus to pull NEW quotes:

- `identity-loss` - Grief for who they used to be as a player/performer/professional.
- `age-regression` - "I was better at 25" language. Comeback-player frame.
- `invisibility` - Feeling unseen, dismissed, or not respected by peers.
- `mouthpiece-objections` - Gear-related pain. Equipment blame.
- `technical-confusion` - "I don't understand what I'm doing wrong" language.
- `embarrassment` - Shame around playing in public or with peers.
- `plateau-frustration` - "I work hard and go nowhere" language.
- `financial-doubt` - "Is this worth the money" objection surfacing.
- `time-doubt` - "Will I have time to do this right" objection.
- `skeptical-of-coaches` - "I've been burned by other programs" frame.
- `accountability-craving` - "I need someone to hold me to it" language.
- `community-craving` - "I want to play with other people like me" language.
- `breakthrough-moment` - The specific turning point in a customer's journey.
- `unexpected-outcome` - What they gained that they didn't expect to gain.
- `sunk-cost-frame` - "I've invested so much in this hobby already" language.
- `legacy-frame` - "I want to leave something behind" or "pass this on" language.

## How to add a new angle

1. Pick a short kebab-case slug.
2. Write a one-sentence description of what this angle surfaces.
3. Add it to the list above.
4. Invoke `/coaching-db mine <new-angle>`.

## Angle selection for content creation

When the downstream content generator asks "what angle should I pick?", consult:

- **TOFU hooks** pull best from: `identity-loss`, `age-regression`, `invisibility`, `plateau-frustration`, `embarrassment`.
- **MOFU ad copy** pulls best from: `what-they-tried`, `mouthpiece-objections`, `technical-confusion`, `skeptical-of-coaches`.
- **BOFU email closers** pull best from: `breakthrough-moment`, `unexpected-outcome`, `specific-result`, `recommendation`.
- **Email subjects** pull best from: `identity-loss`, `invisibility`, `plateau-frustration` (all short and vivid).
- **Carousel slides** pull best from: `before-after`, `transformation`, `what-they-tried` (narrative structure).

If the downstream request is vague, default to `before-state` + `transformation` + `why-harrison` as the three-angle starter set.
