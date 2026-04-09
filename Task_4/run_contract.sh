pip install reportlab --break-system-packages
python3 create_contract_pdf.py
python3 pdf.py real_contract.pdf fraudulent_contract.pdf

files=("collision1.pdf" "collision2.pdf")
 
echo "MD5:"
md5sum collision1.pdf collision2.pdf | awk '{print $2"  "$1}'

echo ""
echo "SHA-256:"
sha256sum collision1.pdf collision2.pdf | awk '{print $2"  "$1}'
