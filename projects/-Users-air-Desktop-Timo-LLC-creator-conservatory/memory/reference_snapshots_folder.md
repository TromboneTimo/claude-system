---
name: Snapshots Folder Location
description: Timo's screenshots live at ~/Desktop/Snapshotsss/ (three s's). When he pastes a screenshot into chat and asks to use it, grab the latest matching file from there. Do not tell him the paste wasn't saved.
type: reference
originSessionId: bb11f5ff-044e-47bd-9a9d-ecc9b0a26bf5
---
When Timo pastes a screenshot into the chat and references "the image" or "the screenshot" or "this image," the file is at `~/Desktop/Snapshotsss/` (note: three s's, not two).

**Full path:** `/Users/air/Desktop/Snapshotsss/`

**Filenames:** macOS default `Screenshot YYYY-MM-DD at H.MM.SS AM/PM.png`.

**How to find the one he just sent:** sort by mtime, take the most recent file or two. `ls -lt /Users/air/Desktop/Snapshotsss/ | head` and match by timestamp against the conversation turn.

**Filename access gotcha:** filenames sometimes contain non-standard space characters (non-breaking space or similar Unicode lookalike) that fail under direct quoted paths. Use glob patterns instead:

```bash
cp /Users/air/Desktop/Snapshotsss/Screenshot*YYYY-MM-DD*H.MM.SS*.png <destination>
```

A direct `cp "Screenshot 2026-04-21 at 2.17.15 PM.png"` WILL fail even when `ls` shows the file. The glob bypasses the encoding issue.

**What NOT to do:** Do not say "I can't find the screenshot" or "the paste didn't save to disk." The paste DID save, it's in Snapshotsss. Check there FIRST before saying you can't access it. 2026-04-21: Timo called this out directly after I spent two turns claiming I couldn't see a screenshot that was right there.

**Also:** there's a second folder at `~/Desktop/SnapShots/` (two s's, different capitalization) but that one appears to be older archive content. Default to Snapshotsss for recent pastes.

**Deliberately-named files (2026-04-28+):** Timo also drops deliberately-named files into Snapshotsss with descriptive names like `usethis.png`, `usethisinstead.png`. When he says "use the [name] file" or "I dropped [name] in the folder," look for the named file directly via `find ~/Desktop/Snapshotsss/ -iname "<name>*"` rather than the Screenshot pattern. He explicitly told me 2026-04-28 to remember this folder so I do not waste turns hunting. Always check Snapshotsss FIRST when he references any image he says he provided.
