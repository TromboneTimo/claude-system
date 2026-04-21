<?xml version="1.0" encoding="UTF-8"?>
<!-- Moderate engraving style (DEFAULT for music-engraving-polisher).
     Dorico defaults with tightened spacing and better collision avoidance.
     Based on MuseScore 4 defaults, overriding values per Elaine Gould's
     Behind Bars recommendations. -->
<museScore version="3.01">
  <Style>
    <!-- Page layout: letter, modest margins -->
    <pageWidth>8.5</pageWidth>
    <pageHeight>11</pageHeight>
    <pagePrintableWidth>7.5</pagePrintableWidth>
    <pageEvenLeftMargin>0.5</pageEvenLeftMargin>
    <pageOddLeftMargin>0.5</pageOddLeftMargin>
    <pageEvenTopMargin>0.5</pageEvenTopMargin>
    <pageOddTopMargin>0.5</pageOddTopMargin>
    <pageEvenBottomMargin>0.75</pageEvenBottomMargin>
    <pageOddBottomMargin>0.75</pageOddBottomMargin>

    <!-- Staff + system spacing (units = staff spaces).
         staffDistance = 7sp gives generous clearance for dynamics + articulations.
         minSystemDistance = 9sp prevents cramped wind + string blocks. -->
    <staffUpperBorder>7</staffUpperBorder>
    <staffLowerBorder>7</staffLowerBorder>
    <staffDistance>7</staffDistance>
    <akkoladeDistance>6.5</akkoladeDistance>
    <minSystemDistance>9</minSystemDistance>
    <maxSystemDistance>15</maxSystemDistance>

    <!-- Lyrics spacing: clear baseline + minimum kerning -->
    <lyricsPlacement>1</lyricsPlacement>
    <lyricsPosAbove x="0" y="-2"/>
    <lyricsPosBelow x="0" y="3"/>
    <lyricsMinTopDistance>1.5</lyricsMinTopDistance>
    <lyricsMinBottomDistance>2</lyricsMinBottomDistance>
    <lyricsLineHeight>1</lyricsLineHeight>
    <lyricsDashMinLength>0.4</lyricsDashMinLength>

    <!-- Bar number placement + frequency -->
    <showMeasureNumber>1</showMeasureNumber>
    <showMeasureNumberOne>0</showMeasureNumberOne>
    <measureNumberInterval>1</measureNumberInterval>
    <measureNumberSystem>1</measureNumberSystem>

    <!-- Minimum note spacing. 1.2 is Dorico-ish; tighter than MuseScore default 1.1 -->
    <minNoteDistance>1.2</minNoteDistance>
    <barNoteDistance>1.2</barNoteDistance>
    <noteBarDistance>1.2</noteBarDistance>
    <measureSpacing>1.5</measureSpacing>

    <!-- Beam slope policy: flat beams where possible, avoid extreme angles -->
    <beamWidth>0.5</beamWidth>
    <beamMinLen>1.316178</beamMinLen>
    <beamNoSlope>0</beamNoSlope>

    <!-- Stem policy -->
    <stemWidth>0.13</stemWidth>
    <stemSlashThickness>0.2</stemSlashThickness>

    <!-- Slur + tie defaults -->
    <SlurEndWidth>0.07</SlurEndWidth>
    <SlurMidWidth>0.2</SlurMidWidth>
    <SlurDottedWidth>0.15</SlurDottedWidth>
    <MinTieLength>1</MinTieLength>
    <SlurMinDistance>0.5</SlurMinDistance>

    <!-- Dynamics: minimum 1sp clearance from staff -->
    <dynamicsPlacement>1</dynamicsPlacement>
    <dynamicsPosAbove x="0" y="-2"/>
    <dynamicsPosBelow x="0" y="3"/>
    <dynamicsMinDistance>0.5</dynamicsMinDistance>

    <!-- Hairpin placement: clear of dynamics -->
    <hairpinPlacement>1</hairpinPlacement>
    <hairpinPosAbove x="0" y="-3.5"/>
    <hairpinPosBelow x="0" y="3.5"/>
    <hairpinHeight>1.2</hairpinHeight>
    <hairpinContHeight>0.5</hairpinContHeight>
    <hairpinLineWidth>0.13</hairpinLineWidth>

    <!-- Articulations: standard placement above for stem-down, below for stem-up -->
    <articulationMag>1</articulationMag>
    <articulationAnchorDefault>0</articulationAnchorDefault>
    <articulationMinDistance>0.5</articulationMinDistance>

    <!-- Accidentals: min column spacing -->
    <accidentalNoteDistance>0.22</accidentalNoteDistance>
    <accidentalDistance>0.3</accidentalDistance>

    <!-- Ledger lines -->
    <ledgerLineWidth>0.16</ledgerLineWidth>
    <ledgerLineLength>0.35</ledgerLineLength>

    <!-- Rehearsal mark: clear of staff + frame padding -->
    <rehearsalMarkPlacement>0</rehearsalMarkPlacement>
    <rehearsalMarkPosAbove x="0" y="-3.5"/>
    <rehearsalMarkFrameType>1</rehearsalMarkFrameType>
    <rehearsalMarkFramePadding>0.5</rehearsalMarkFramePadding>
    <rehearsalMarkFrameWidth>0.15</rehearsalMarkFrameWidth>

    <!-- Tempo text: above staff, clear of rehearsal mark -->
    <tempoPlacement>0</tempoPlacement>
    <tempoPosAbove x="0" y="-4"/>

    <!-- Multi-measure rests: minimum 2 bars before consolidating -->
    <createMultiMeasureRests>0</createMultiMeasureRests>
    <minEmptyMeasures>2</minEmptyMeasures>
    <minMMRestWidth>4</minMMRestWidth>

    <!-- System breaks: never cast off fewer than 4 measures per system unless forced -->
    <minMeasureWidth>5</minMeasureWidth>

    <!-- Chord symbols (for jazz / lead sheets) -->
    <chordSymbolPosAbove x="0" y="-2.5"/>
  </Style>
</museScore>