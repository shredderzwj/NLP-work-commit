@echo OFF
cd /d %~dp0
SET /p inpath="���� wiki ���Ͽ��ļ�����·����"
SET /p outpath="��������ļ���·����"
SET /p minlenth="������С�ı����ȣ�"
python WikiExtractor.py --min_text_length %minlenth% -o "%outpath%" -b 20G "%inpath%"
ECHO.
ECHO job done��
PAUSE 