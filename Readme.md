# Resturant Bot NLU Demo

## Installation

Please run following

```
pip install -r requirments.txt
```

### To Run

rasa run  -m models/20230511-013837-isothermal-photon.tar.gz --enable-api

### To Use

Send post request to

http://0.0.0.0:5005/model/parse

```{
{
	"text":" Your Text Here"
}
```
