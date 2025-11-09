# 🏃‍♂️ Dados, performance e curiosidade: analisando minhas corridas e caminhadas dos últimos 12 meses 📊  

Recentemente, decidi unir duas coisas que gosto bastante: **dados e corrida**.  
Eu queria entender como poderia **melhorar meu desempenho** analisando os treinos dos últimos 12 meses — por exemplo, **qual o melhor horário do dia para correr**, ou **quando meu rendimento é melhor**.  

O problema é que o app do meu smartwatch (*Haylou*) não oferece uma forma de exportar todos os dados de treino. Então, montei uma pequena jornada de engenharia de dados:  

- Integrei a **Haylou com a Strava** para centralizar tudo;  
- Baixei os dados completos da Strava, que vieram em várias pastas cheias de arquivos `.fit.gz`;  
- Criei um **script em Python** com `fitdecode`, `gzip` e `pandas` para:  
  - Descompactar todos os arquivos  
  - Ler os registros de cada treino  
  - Consolidar tudo em um **DataFrame**  
  - E gerar um **CSV** pronto para o Power BI.  

No **Power BI**, ajustei as tipagens e formatações, criei uma **coluna de período do dia** e usei **DAX** para calcular o *pace* (já que o tempo vinha em segundos e a distância em km).  

## 📈 Resultados e insights  

- 🔥 Gastei **34 mil calorias** entre corridas e caminhadas;  
- 🏃‍♂️ Foram **522 km só em corridas**;  
- 🌅 Meus **melhores paces** acontecem pela manhã e à noite;  
- ☀️ **Melhor relação distância x pace** no período da manhã.  

Um projeto rápido, mas que mostra o quanto **nossos próprios dados podem nos ajudar a evoluir**, mesmo fora do ambiente corporativo.  
No fim, o objetivo era simples: **usar dados para entender como posso correr melhor** — e funcionou 🧠💪  

---

> *Esse projeto foi desenvolvido em Python e Power BI, utilizando dados extraídos do Strava via integração com o smartwatch Haylou.*  

📁 **Tecnologias utilizadas:** `Python`, `fitdecode`, `pandas`, `gzip`, `Power BI`, `DAX`  

#️⃣ **Hashtags:**  
`#DataAnalytics` `#Python` `#PowerBI` `#Strava` `#DataScience` `#SportsData` `#DataEngineering` `#Visualization` `#PersonalAnalytics` `#ETL` `#Running`
