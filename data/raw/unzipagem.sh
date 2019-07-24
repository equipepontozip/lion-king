echo "EH HORA DE DEZIPAR!!!"
unzip acessogov-20190723T170055Z-001.zip &&
cd ./acessogov &&
FILES="Auditoria_1a5.zip
Auditoria_6a10.zip
Auditoria_Aplicacao_1.csv.zip
Auditoria_Aplicacao_2.csv.zip
Auditoria_Aplicacao_3.csv.zip
Auditoria_Aplicacao_4.csv.zip
Auditoria_Aplicacao_5.csv.zip
Auditoria_Aplicacao_6.csv.zip"
for f in $FILES
do
 echo "Processing $f"
 unzip $f
done
