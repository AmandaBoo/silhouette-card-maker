## Misc Supploes
- 3 cutting mats
- 3-4 sticky notes
- 1 cermaic xacto knife
- 1 cutting mat 
- 1 scissors
- pen

## Single Sided Cards
1. create .txt file in decklist folder in moxfield format
2. run moxfield.sh $filename_sans_txt_extension to query for art
3. check image count in folder (use mac finder for easy counting) and fill in blank spots with land or tokens (each page prints 8 cards)
4. run front_pdf.sh to create pdf file (configurations already loaded into the python script itself)
5. Double check game.pdf to verify correct art was selected
    - Tweak .txt file and rerun steps 2-5 as needed
6. Rename file as needed
7. Print pdf with
    - koala photo paper
    - Printer settings : glossy photo paper, quality best, scale 100% (these settings should already be programmed into the printer view)
8. Laminate
9. Cut with Force 33, Speed 20, Depth 7, Pass 3

### Notes on single sided printing
- It takes about 3 minutes 48 seconds to print a single sheet (50 minutes for 13 sheets)
- 4 minutes to put the cards in laminate pouches (~19 seconds a sheet)
- 13 minutes for the lamination machine to run (1 minutes/sheet)
- 30 minutes to cut (assuming no mis-cuts and practically no silhouette registration errors) (2 min 19 seconds/sheet)
- 6 minutes to laminate a 104 cut cards 

## Double-sided cards (only work with 8 cards/1 page at a time)
1. create .txt file in decklist folder in moxfield format
2. run moxfield.sh $filename_sans_txt_extension to query for art
3. check image count in folder (use mac finder for easy counting) and fill in blank spots with land or tokens (each page prints 8 cards).
    - Don't worry about finding additional double-sided cards if there aren't any
4. run doublesided_pdf.sh to create pdf file (configurations already loaded into the python script itself).
    - offsets may need to be reconfigured. If so, print out
5. Double check game.pdf to verify correct art was selected
    - Tweak .txt file and rerun steps 2-5 as needed
6. Rename file as needed
7. Print page 1
    - koala photo paper
    - Printer settings : glossy photo paper, quality best, scale 100% (these settings should already be programmed into the printer view)
8. Take printed paper and flip it over to the other side by turning the page to the right or left. Reinsert into printer
9. Print page 2
10. Laminate and cut

## Foil printing (only work with 8 cards/1 page at a time)
1. create .txt file in decklist folder in moxfield format
2. run moxfield.sh $filename_sans_txt_extension to query for art
3. check image count in folder (use mac finder for easy counting) and fill in blank spots with land or tokens (each page prints 8 cards).
    - Don't worry about finding additional double-sided cards if there aren't any
4. run doublesided_pdf.sh to create pdf file (configurations already loaded into the python script itself).
    - offsets may need to be reconfigured. If so, print out
5. Double check game.pdf to verify correct art was selected
    - Tweak .txt file and rerun steps 2-5 as needed
6. Rename file as needed
7. Prepare paper
    - Stick foil sticker paper onto cardstock paper. (use this video as reference : https://www.youtube.com/watch?v=QQa9m5HZlxA)
    - Trim excess cardstock paper with xacto knife. Do NOT cut the foil paper
8. Print page 1
    - koala photo paper
    - Printer settings : glossy photo paper, quality best, scale 100% (these settings should already be programmed into the printer view)
9. Take printed paper and flip it over to the other side by turning the page to the right or left. Reinsert into printer
10. Print page 2
11. Laminate and cut

## Printing whiteboard blank cards (doesn't curently work double-sided)
1. Use either the outline or blank mtg card pngs and create sets of 8 of these images in the "front" folder
2. run front_pdf.sh to create pdf file (configurations already loaded into the python script itself)
3. Double check game.pdf to verify it looks correct
    - Tweak .txt file and rerun steps 2-5 as needed
4. Rename file as needed
5. Print pdf with
    - 270gsm cardstock paper
    - Printer settings : glossy photo paper, quality best, scale 100% (these settings should already be programmed into the printer view)
6. Laminate with WHITEBOARD COMPATIBLE LAMINATE
   7. Cut with Force 33, Speed 20, Depth 10, Pass 8 (8 is probably too high. Try 5-7 next time) 