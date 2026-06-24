# Workspace Memory Index

- [Uppercase breaks CJK](feedback_uppercase_breaks_cjk.md). CSS `text-transform: uppercase` corrupts Japanese/Chinese/Korean and emoji flags, add `normal-case` override.
- [Narrate long generations](feedback_narrate_long_generations.md). Send a heads-up before any tool call that will take >20s of silent output, silence reads as a stall.
- [Interrupts preempt work](feedback_interrupts_preempt_work.md). Quick user asks mid-task jump the queue, do them first, do not queue behind big writes.
- [Skip gpt-taste preflight when prescriptive](feedback_skip_gpt_taste_preflight_when_prescriptive.md). If the brief already names fonts/layout/motion, skip the Python RNG ceremony and execute.
- [Search inside clients/, not workspace root](feedback_search_clients_dir.md). Real code lives in clients/<name>/, the bare root has no src/. Grep clients/ before claiming a page does not exist.
- [Sample pixels before cropping](feedback_sample_pixels_before_cropping.md). Print edge RGB values of a source image before picking any trim threshold, do not guess.
- [Pad with exact container bg](feedback_pad_with_exact_container_bg.md). Non-square trimmed images padded to square must use the downstream container bg from the data file, per-item. Never black-by-default.
- [Verify both languages](feedback_verify_both_languages.md). After touching any lang-aware component, grep for hardcoded English AND toggle JA in browser. SIDE A/B and track titles bit me on Samurai Brass.
- [Enumerate failure axes before shipping](feedback_enumerate_failure_axes_before_shipping.md). For any visual bug, list source/data/CSS/component/animation/lang axes up front. Iterating 3+ times = first enumeration was incomplete.
- [Cap Next.js image deviceSizes in config](feedback_cap_next_image_device_sizes.md). Default ships 3840px fallback for every `<Image>`. For image-heavy pages, set capped `deviceSizes`/`imageSizes` in next.config.ts. Verify by grepping deployed HTML srcSet.
- [Audit static asset sizes before every deploy](feedback_audit_static_assets_before_deploy.md). `find public -size +1M` before any vercel push. A single 18MB video kills perf no matter how clever the code.
- [Measure real page weight, do not claim wins without numbers](feedback_measure_real_page_weight.md). After any perf task, curl the deployed URL and grep srcSet. No byte counts = no claim of a win.
- [Autoplay videos need a silent audio track](feedback_autoplay_video_needs_audio_track.md). Never `-an` a hero video, browsers refuse autoplay without audio stream. Inject silent AAC. Verify by opening in Safari, not just ffprobe.
- [Custom quality prop requires config](feedback_next_quality_prop_requires_config.md). `quality={78}` on `<Image>` returns HTTP 400 on Vercel unless 78 is in `images.qualities`. Default 75 only works by default.
- [Pre-size image sources](feedback_pre_size_sources_for_image_optimizer.md). Cold image optimizer is slow on 700KB+ sources. Resize to max 2x display width with sips before deploy.
- [Visual QA must include interacted states](feedback_visual_qa_interacted_states.md). Render and read playing/hovered/scrolled state, not just first paint. Native `<video controls>` defaults are hideous and only appear after click.
- [Local preview, not Vercel, for visual checks](feedback_local_preview_before_deploy.md). Run `npm run dev` and open localhost in Safari. Don't deploy to Vercel just to eyeball changes.
