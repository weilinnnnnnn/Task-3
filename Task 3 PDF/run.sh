pip install reportlab --break-system-packages
python3 create_pdf.py
python3 pdf.py file1.pdf file2.pdf

files=("collision1.pdf" "collision2.pdf")

echo "MD5:"
md5sum collision1.pdf collision2.pdf | awk '{print $2"  "$1}'

echo ""
echo "SHA-256:"
sha256sum collision1.pdf collision2.pdf | awk '{print $2"  "$1}'
