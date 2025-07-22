Hardware utilizado:

• Processador: Ryzen 5 5600
• Memória Ram: 16GB DDR4
• Sistema Operacional (SO): Windows 10


Linguagem de programação escolhida:

• Os algoritmos foram implementados na linguagem Python, no ambiente
Jupyter Notebook.

• Bibliotecas: time, random, pandas, matplotlib, seaborn

Conclusão:

A análise prática dos algoritmos de busca sequencial e binária evidenciou
claramente o impacto da complexidade computacional sobre o desempenho. A
busca sequencial apresentou crescimento linear no número de comparações e no
tempo de execução, conforme o tamanho da entrada aumentava, especialmente
no pior caso. Já a busca binária demonstrou crescimento logarítmico em todos os
casos, mantendo um desempenho altamente eficiente mesmo com grandes
volumes de dados.
O comportamento prático observou-se alinhado com a análise assintótica
esperada: O(n) para a busca sequencial (caso médio e pior) e O(log n) para a
busca binária, tanto em tempo quanto em número de comparações.

Vantagens e Limitações dos Algoritmos Avaliados

Busca Sequencial:
• Vantagens: Simplicidade de implementação; funciona em qualquer tipo de
lista (ordenada ou não).

• Limitações: Desempenho ineficiente para listas grandes; custo de tempo
proporcional ao tamanho da entrada.

Busca Binária:

• Vantagens: Alto desempenho em estruturas ordenadas; número de
comparações cresce lentamente.

• Limitações: Exige que os dados estejam previamente ordenados;
Reflexão sobre a Complexidade Computacional

Os resultados reforçam a importância de considerar a complexidade
computacional ao escolher algoritmos de busca em aplicações reais. Em
sistemas com grandes volumes de dados, a escolha errada pode gerar gargalos de
desempenho. A busca binária, por sua complexidade logarítmica, é ideal em
situações com dados ordenados. Já a busca sequencial, apesar de simples, só é
viável para conjuntos pequenos ou não ordenados. Portanto, compreender e
aplicar os conceitos de análise assintótica é fundamental para soluções mais
eficazes e escaláveis.
