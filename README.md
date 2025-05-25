# fl_data_bot
this is pandas dataframe tool integration example (from langchain)
data used for test is from https://www.kaggle.com/datasets/shohinurpervezshohan/freelancer-earnings-and-job-trends?select=freelancer_earnings_bd.csv

Jupiter Notebook contains steps with examples how to use this tool
main.py contains the code to run the tool in a command line style

set .env with your API key
```bash
QWEN_API_KEY=sk-your-api-key
```
# Installation and usage
```bash
git clone ```https://github.com/dmitrydolnikov/lg_time_bot.git```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
````
example of how to run the tool:
(use -v or -verbose to see the detailed tool output)
```bash
1.single run and exit
```bash
python main.py "how many freelancers there are in data set?"
```
2. run in a loop
```bash
python main.py
```

#questions examples

- how much more profitable freelancers taking crypto?
- How many freelancers are there in the dataset?
- What is the distribution of earnings among freelancers?
- how many freelancers there are per client country?
- What is the average earnings per freelancer in the USA?
- Насколько выше доход у фрилансеров, принимающих оплату в криптовалюте, по сравнению с другими способами оплаты?
- Как распределяется доход фрилансеров в зависимости от региона проживания?
- Какой процент фрилансеров, считающих себя экспертами, выполнил менее 100 проектов?
