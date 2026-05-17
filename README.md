# Everything (Anki deck)

## Overview

I have had some good fun creating various bespoke Anki card templates, but not having them under VCS makes making changes to any of them a rather daunting prospect. This repo contains a single `deck-stripped.json` produced after stripping the cards from a CrowdAnki-produced `deck.json`, allowing me to version my templates.

Feel free to use them for yourself.

## (Partial) list of note types

### Article Cloze

My go-to template for learning anything. Essentially a standard typed Cloze template but with an extra ``[[...]]`` cloze type; this is used for clozing text without requiring the user to type it. Useful for bodies of text where a certain key term is referred to in multiple places.

JP Article Cloze is an alternative version for extracts taken from text in Japanese. The only difference is the choice of font.

### CN/JP Encountered Vocab; Korean Vocab; できる韓国語

Cards with both reading and meaning fields; fairly self-explanatory. CN uses a font that can correctly display simplified characters; JP uses a font that can correctly display shinjitai. Korean Vocab uses a font that can correctly display hanja; できる韓国語 is a JP/KR version that I use for the textbook I am following.

I understand that I'm using the country codes instead of the language codes, but I can't be bothered to change them over.

### Code

I use these to memorise snippets of code. Code (Cloze) was my first attempt at making such a template. Code (Editor) is the one that should be used.

Code (Editor) and Code (SQL) contain an Ace editor along with diff.js to calculate the diffs between the expected answer and the user's typed answer. Code (SQL) also contains a browser SQLite library to allow for evaluation of the typed answer.

### Navigation

I was fed of not knowing how to drive around my local area or getting around Soho without a map, so I made this template. Inside is a Leaflet embedded map with a custom "tap to place marker" feature that allows the user to pinpoint locations on the map. The idea is that an image taken from something like Google Street View is displayed to the user, and the user then pinpoints where that is on the map.

### Proof

This is really just a slightly modified version of Enhanced Cloze. When writing proofs, it doesn't make sense to be able to see future clozes from the current proof, so this ensures than any future clozes remain clozed until the user decides to flip the card.

### Q&A

To be honest, I'm not too sure why I gave this a new name. This is literally just the Basic note type but with some formatting to make it look more like the other card types.
