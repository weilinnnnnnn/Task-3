# Practical Collision Attacks

# Task 2 Collision-generating Techniques
## Overview
We are investigating the different types of collision-generating techniques. To do so, we demonstrate IPC using FastColl and UniColl, CPC using FastCPC and reusable collisions using formatting tricks using the precomputed examples from the corkami repository. These are built on top of HashClash by Marc Stevens (https://github.com/cr-marcstevens/hashclash) and corkami/collisions (https://github.com/corkami/collisions) by Ange ALbertini.

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

# Task 3 Unicoll Collision for PDF Files
## Overview
We are demonstrating identical prefix collision attack on PDF files. Two PDF files with different visible content are generated using the reportlab library and then fed into a collision script to produce two different output files (collision1.pdf, collision2.pdf) that have identical MD5 hashes but different content.

## Prerequisites
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


## Credits
The collision script 'pdf.py' is taken from the corkami/collisions repository by Ange Albertini (https://github.com/corkami/collisions), with some modifications to fix Python 3.12 compatibility issues. 
The follwing files are also taken from the corkami/collisions repository by Ange Albertini (https://github.com/corkami/collisions):
 - dummy.pdf
 - pdf1.bin
 - pdf2.bin


