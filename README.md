# Degree Global Forecast Grids

## Download dos arquivos de dados

Site da NCAR para acesso ao banco de dados

https://rda.ucar.edu/datasets/ds084.1/dataaccess/

## GribFTP 

É possível acessar um site FTP, sem necessidade de login, para baixar os arquivos 'grib2'. 

Links do FTP:

https://app.globus.org/file-manager?origin_id=b6b5d5e8-eb14-4f6b-8928-c02429d67998&origin_path=%2Fds084.1%2F&two_pane=false

https://thredds.rda.ucar.edu/thredds/catalog/catalog_ds084.1.html

Dados de 2015 até o presente

Formato dos arquivos:

- gfs.0p25.2023010100.f000.grib2

Esses arquivos possuem muitas informações com quase meio Gigabytes de memoria. 

## Procedimento de Instalação


Para a leitura desses arquivos, é imprescindível a instalação das seguintes bibliotecas em Python:

- pygrib (biblioteca principal responsável pela leitura dos dados)
- xarray (utilizada para conversão, oferecendo maior versatilidade na manipulação dos dados)
- netCDF4 (empregada na conversão dos dados)
Em caso de ocorrência de erros durante o processo de compilação, poderá ser necessário instalar algumas bibliotecas adicionais.

### Considerações Importantes

Caso queira trabalhar diretamente com os dados usando pygrib, fique a disponsão. Contudo, para um primeiro contato com esse formato, achei um tanto complicado a manipulação dos dados. O que pode variar com os seus objetivos. 

Portanto, optei por selecionar algumas variaveis e suas dependencias e sava-los em arquivo netCDF. 

No meu caso, consegui instalar a biblioteca pygrib apenas em meu ambiente WSL com Ubuntu, onde realizei a conversão para um arquivo netCDF (.nc).

Durante o procedimento de redução de dados, optei por selecionar exclusivamente as matrizes referentes às componentes do vento (U e V) em todos os níveis de pressão disponíveis. Posteriormente, salvei os dados e elaborei um gráfico exemplificativo. 

De qualquer forma estou a disposição para ajudar em algo mais. 

Ps. compactei os dados para poder subir no repositorio