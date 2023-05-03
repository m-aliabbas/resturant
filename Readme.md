# Resturant Bot NLU Demo

## Installation

Please run following 

```
pip install -r requirments.txt
```

### To Run


rasa run  -m models/20230503-010724-diagonal-bogey.tar.gz --enable-api 

### To Use

Send post request to 

localhost:port/models/parse

```{
{
	"text":" Your Text Here"
}
```
