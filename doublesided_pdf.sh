# run with ./doublesided_pdf.sh
# to be used with foil and with double sided cards
python create_pdf.py --load_offset --front_dir_path game/front/"$1" --back_dir_path game/back/"$2" --output_path game/output/"$1".pdf --name "$1"