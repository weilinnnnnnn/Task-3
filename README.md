# Practical Collision Attacks
Cryptographic hash functions are mathematical algorithms that map inputs of arbitrary size to a fixed-length sequence of characters, also known as a hash value or digest. The security of these applications depends on the assumption that it is computationally infeasible to generate two different inputs that map to the same hash, also known as collision resistance. However, this assumption has been eroded for certain hash functions such as MD5 (Message Digest Algorithm 5) and SHA-1(Secure Hash Algorithm 1), which were some of the most prevalent hash functions in the history of digital security. We will primarily focus on MD5 in this project.

# Task 2 Collision-generating Techniques
## Overview
We are investigating the different types of collision-generating techniques. To do so, we demonstrate IPC using FastColl and UniColl, CPC using FastCPC and reusable collisions using formatting tricks using the precomputed examples from the corkami repository. These are built on top of HashClash by Marc Stevens (https://github.com/cr-marcstevens/hashclash) and corkami/collisions (https://github.com/corkami/collisions) by Ange Albertini.

## Compilation and Installation
### Clone the repository 
```bash
git clone https://github.com/weilinnnnnnn/Practical-Collision-Attack
```

## Running the collisions
### Identical-Prefix Collisions
#### FastColl
```bash
cd fastcoll_run
# prefix is "prefix"
time ../bin/md5_fastcoll -p ipc_prefix.bin -o fastcoll1.bin fastcoll2.bin
```
Expected output:
``` bash
MD5 collision generator v1.5
by Marc Stevens (http://www.win.tue.nl/hashclash/)

Using output filenames: 'fastcoll1.bin' and 'fastcoll2.bin'
Using prefixfile: 'ipc_prefix.bin'
Using initial value: c11b028f865667bf0b5c2b9f17601e77

Generating first block: ........
Generating second block: S00.......
Running time: 1.71593 s
../bin/md5_fastcoll -p ipc_prefix.bin -o fastcoll1.bin fastcoll2.bin  1.71s user 0.01s system 99% cpu 1.733 total
```
To verify:
``` bash
md5sum fastcoll1.bin fastcoll2.bin      # match
sha256sum fastcoll1.bin fastcoll2.bin   # differ
```
We display sha256 hashes to show that the content of the files are different

#### UniColl
```bash
cd unicoll_run
time ../scripts/generic_ipc.sh ipc_prefix.bin
```
To verify:
``` bash
md5sum collision1.bin collision2.bin      # match
sha256sum collision1.bin collision2.bin   # differ
```

### Chosen-Prefix Collisions
We ran FastCPC as a demonstration
```bash
cd fcpc_run
# "Hello, I am file A" > fcpc_prefix_a.bin
# "Hello, I am file B" > fcpc_prefix_b.bin
# Verify they are different
md5sum fcpc_prefix_a.bin fcpc_prefix_b.bin
```
We started the RAM logger in a separate terminal
``` bash
while true; do
    echo "=== $(date '+%H:%M:%S') ===" >> ram.log
    top -l 1 -s 0 | grep PhysMem >> ram.log
    ps aux | grep md5_ | grep -v grep >> ram.log
    echo "" >> ram.log
    sleep 30
done
```

Running FastCPC
``` bash
# ../scripts/fastcpc.sh fcpc_prefix_a.bin fcpc_prefix_b.bin 2>&1 | tee cpc.log
```

Verify output
``` bash
md5sum file1_7.bin file2_7.bin # match
sha256sum file1_7.bin file2_7.bin #differ
```

### Reusable Collisions using Formatting Tricks
We used the precomputed prefix pairs for the JPG format from the corkami repository. The JPG script uses jpg1.bin and jpg2.bin, which are precomputed UniColl blocks already aligned with JPG's comment segment structure.
``` bash
cd rc_run
time python3 jpg.py jpg1.bin jpg2.bin
```

To verify:
``` bash
md5sum collision1.jpg collision2.jpg # match
sha256sum collision1.jpg collision2.jpg # differ
```

# Task 3 
## Overview
We are demonstrating identical prefix collision attack on PDF and TXT files. Two PDF files with different visible content are generated using the reportlab library and then fed into a collision script to produce two different output files (collision1.pdf, collision2.pdf) that have identical MD5 hashes but different content. Two TXT files with identical visble content are generated using a prefix creation script then fed into corkami's collision script to produce two different output files (collision1.txt, collision2.txt) that have identical MD5 hashes but same content and different collision blocks (suffixes).

## 1. Unicoll Collision for PDF Files
### Prerequisites
 - Docker

## Installation and Setup
### Create a Ubuntu 24.04 container
```bash
docker run -it --name collision ubuntu:24.04 bash
```
### Download dependencies inside the container
```bash
apt update && apt install -y git python3 python3-pip 
```
### Clone the repository 
```bash
git clone https://github.com/weilinnnnnnn/Practical-Collision-Attack
```
### Build mutool 1.18
```bash
apt install -y wget && wget https://mupdf.com/downloads/archive/mupdf-1.18.0-source.tar.gz && tar -xzf mupdf-1.18.0-source.tar.gz && cd mupdf-1.18.0-source && make -j$(nproc) HAVE_X11=no HAVE_GLUT=no
```
## Run the Collision 
Run the shell script which handles everything
```bash
cd /Practical-Collision-Attack
bash run.sh
```
This will 
 1. Install Python dependency ReportLab
 2. Generate two different input PDF files (file1.pdf, file2.pdf) using create_pdf.py
 3. Run the MD5 collision attack script (pdf.py)
 4. Output the MD5 and SHA-256 hashes of the collision files

## Interpreting the Output
Both the collision PDF files generated will have the same MD5 but diffferent SHA-256 and they are displaying different content.

## 2. Collision for TXT Files
## Installation and Setup
### Clone the repository 
```bash
git clone https://github.com/corkami/collisions.git
```

## Run the Collision
### Create a folder for TXT Collisions
```bash
mkdir txt_workdir && cd txt_workdir
```

### Run the make_prefix file
```bash
python3 make_prefix.py
```

### Run the Collision Generation
```bash
../scripts/generic_ipc.sh prefix.pdf
```

## Checking the Hashes
### Verify hash of each file
```bash
md5 collision1.bin collision2.bin
```

### Show byte differences between files
```bash
diff <(xxd collision1.bin) <(xxd collision2.bin)
```

### Convert .bin files to .txt by renaming file extension

This will 
 1. Generate one TXT file with the identical prefix (prefix.txt) using make_prefix.py
 2. Run the corkami MD5 collision attack script (generate_ipc.sh)
 3. Output the MD5 and byte differences of the collision files

## Credits
The collision script 'pdf.py' is taken from the corkami/collisions repository by Ange Albertini (https://github.com/corkami/collisions), with some modifications to fix Python 3.12 compatibility issues. 
The follwing files are also taken from the corkami/collisions repository by Ange Albertini (https://github.com/corkami/collisions):
 - dummy.pdf
 - pdf1.bin
 - pdf2.bin


