@echo off
cd /d %~dp0
python WikiExtractor.py --min_text_length 30 -o "D:\wiki" -b 20G "D:\wiki\zhwiki-20190720-pages-articles-multistream.xml.bz2"