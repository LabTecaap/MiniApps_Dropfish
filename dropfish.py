
import streamlit as st
from PIL import Image 
#colocando um título
img=Image.open('dropfish.jpg')
st.image(img)
st.title('app DropFish.py')
st.success('ESTE App FOI DESENVOLVIDO PARA TRABALHAR COM TRÊS ESPÉCIES: TILÁPIA , TAMBAQUI E PIRARUCU ')
option=st.selectbox('SELECIONE A ESPÉCIE',['TILÁPIA','TAMBAQUI','PIRARUCU'])


if option =='TILÁPIA':
    
    seu_desejo=st.text_input('VOCÊ DESEJA VER PARÂMETROS OU ARRAÇOAMENTO?').lower()
   
    if seu_desejo=='parametros' or seu_desejo == 'parâmetros':
        st.success('O Oxigênio Dissolvido ideal é de 3 a 4 mg por litro para tilápia')
        st.success('O pH ideal para a tilápia é de 7 a 8,5')
        st.info('A transparência da água é de 30 cm a 40 cm')
        st.success('A tilápia suporta até 0,5 mg por litro de amônia não ionizada,porém a quantidade ideal de amônia é abaixo de 0,5 mg/l ')
        st.info('A temperatura ideal para a tilápia é de 25 a 32 °C')
        st.warning(' Se os parâmetros do seu cultivo não estiverem de acordo com os valores apresentados, procure um Zootecnista ou um Engenheiro De Pesca para solucionar os problemas')
    if seu_desejo =='arracoamento'or seu_desejo=='arraçoamento':
        img=Image.open('imagem1.jpeg')
        st.image(img)
      
elif option == 'TAMBAQUI' :
    seu_desejo=st.text_input('VOCÊ DESEJA VER PARÂMETROS OU ARRAÇOAMENTO?').lower()
    if seu_desejo== 'parametros' or seu_desejo=='parâmetros' :
        st.success(' O Oxigênio Dissolvido ideal é de 4 mg por litro para tambaqui')
        st.info(' O pH ideal para a Tambaqui é de 6,5 a 8,5')
        st.success('A temperatura ideal para o Tambaqui é 25°C a 32 °C')
        st.info('A transparência da água é de 30 cm a 40 cm')
        st.success('A amônia ideal para o Tambaqui é 0,6 mg/l,porém abaixo é melhor')
        st.warning('Se os parâmetros do seu cultivo não estiverem de acordo com os valores apresentados, procure um Zootecnista ou um Engenheiro De Pesca para solucionar seus problemas')
    if seu_desejo =='arracoamento' or seu_desejo=='arraçoamento':
        img=Image.open('imagem3.jpeg')
        st.image(img)
        
elif option == 'PIRARUCU':
    seu_desejo=st.text_input('QUER VER OS PARÂMETROS OU ARRAÇOAMENTO?').lower()
    if seu_desejo == 'parametros' or seu_desejo=='parâmetros':
        st.success('O Oxigênio Dissolvido ideal é de 2 mg por litro para PIRARUCU')
        st.info('O pH ideal para a PIRARUCU é de 6.5 a 8.5')
        st.success('A temperatura ideal para o PIRARUCU é 28°C a 30°C')
        st.info('A tranparência está entorno de 30 a 45 cm para o PIRARUCU')
        st.success('A amônia ideal para o PIRARUCU é 0.2 a 0.4 mg por litro')
        st.warning('Se os parâmetros do seu cultivo não estiverem de acordo com os valores apresentados, procure um Zootecnista ou um Engenheiro De Pesca para resolver o problema do seu cultivo')
    if seu_desejo =='arraçoamento'or seu_desejo=='arracoamento':
        imagem=Image.open('imagem2.jpeg')
        st.image(imagem)
