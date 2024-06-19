import streamlit as st
import pandas as pd

# Função para verificar as credenciais de login
def verificar_login(username, password):
    dados = pd.read_csv('dados.csv')
    for _, row in dados.iterrows():
        if row['username'] == username and row['password'] == password:
            return True
    return False

# Função para a página de login
def pagina_login():
    st.title('Área de Login')
    username = st.text_input('Nome de Usuário')
    password = st.text_input('Senha', type='password')
    if st.button('Entrar'):
        if verificar_login(username, password):
            st.session_state['logado'] = True
            st.success('Login realizado com sucesso!')
            st.experimental_rerun()
        else:
            st.error('Nome de usuário ou senha incorretos!')

# Função para a página de um sub-tópico
def pagina_subtopico(titulo, video_url, material_url, descricao):
    st.title(titulo)
    st.video(video_url)
    st.markdown(descricao)
    st.markdown(f"[Baixar Material]({material_url})", unsafe_allow_html=True)
    if st.button('Enviar dúvida ao Professor'):
        st.markdown("### Envie sua dúvida")
        with st.form("form_duvida"):
            duvida = st.text_area('Digite sua dúvida aqui...')
            submit = st.form_submit_button('Enviar')
            if submit:
                st.success("Dúvida enviada com sucesso!")

# Função para a página Home
def pagina_home():
    st.title('Bem-vindo ao Curso de Física a Nível Militar')
    st.image('https://www.exemplo.com/imagem_curso.jpg', caption='Curso de Física a Nível Militar', use_column_width=True)
    st.markdown("""
        ## Sobre o Curso
        Este curso é projetado para fornecer uma compreensão profunda dos princípios fundamentais da física, com aplicações específicas ao contexto militar. Explore tópicos desde as Leis de Newton até o Eletromagnetismo e Óptica, com material rico em conteúdo e exemplos práticos.

        ### Objetivos do Curso
        - Fornecer uma base sólida em conceitos de física.
        - Aplicar teorias físicas a situações reais no contexto militar.
        - Preparar os alunos para desafios físicos em operações militares.

        ## Estrutura do Curso
        - **Mecânica**: Estudo do movimento e suas causas.
        - **Eletromagnetismo**: Investigação das forças elétricas e magnéticas.
        - **Óptica**: Exploração da luz e suas interações.
        - **Estática**: Análise das forças em sistemas em equilíbrio.

        ### Recursos
        - Aulas em vídeo.
        - Materiais de leitura.
        - Sessões de dúvidas com professores.
    """)
    st.image('https://www.exemplo.com/imagem_fisica.jpg', caption='Física Aplicada', use_column_width=True)
    st.markdown("Visite [nosso site](https://www.exemplo.com) para mais informações.")

# Função para o menu de tópicos e sub-tópicos
def menu_topicos():
    st.sidebar.title('Menu de Tópicos')
    topico = st.sidebar.selectbox('Escolha o Tópico', ['Home', 'Mecânica', 'Eletromagnetismo', 'Óptica', 'Estática'])

    if topico == 'Home':
        pagina_home()

    elif topico == 'Mecânica':
        subtopico = st.sidebar.selectbox('Escolha o Sub-Tópico', ['Leis de Newton', 'Trabalho e Energia'])
        if subtopico == 'Leis de Newton':
            pagina_subtopico(
                titulo='Leis de Newton',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://classroom.google.com/c/NjE4NzQ4MzcwMTg3/m/NjE4NzY5Nzg0NDU2/details',
                descricao='Descrição da aula sobre as Leis de Newton.'
            )
        elif subtopico == 'Trabalho e Energia':
            pagina_subtopico(
                titulo='Trabalho e Energia',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/trabalhoenergia.pdf',
                descricao='Descrição da aula sobre Trabalho e Energia.'
            )

    elif topico == 'Eletromagnetismo':
        subtopico = st.sidebar.selectbox('Escolha o Sub-Tópico', ['Campo Elétrico', 'Indução Magnética'])
        if subtopico == 'Campo Elétrico':
            pagina_subtopico(
                titulo='Campo Elétrico',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/campoeletrico.pdf',
                descricao='Descrição da aula sobre Campo Elétrico.'
            )
        elif subtopico == 'Indução Magnética':
            pagina_subtopico(
                titulo='Indução Magnética',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/inducomagnetica.pdf',
                descricao='Descrição da aula sobre Indução Magnética.'
            )

    elif topico == 'Óptica':
        subtopico = st.sidebar.selectbox('Escolha o Sub-Tópico', ['Reflexão', 'Refração'])
        if subtopico == 'Reflexão':
            pagina_subtopico(
                titulo='Reflexão',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/reflexao.pdf',
                descricao='Descrição da aula sobre Reflexão.'
            )
        elif subtopico == 'Refração':
            pagina_subtopico(
                titulo='Refração',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/refracao.pdf',
                descricao='Descrição da aula sobre Refração.'
            )
    
    elif topico == 'Estática':
        subtopico = st.sidebar.selectbox('Escolha o Sub-Tópico', ['Condições de equilíbrio', 'Centro de massa'])
        if subtopico == 'Condições de equilíbrio':
            pagina_subtopico(
                titulo='Condições de equilíbrio',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/reflexao.pdf',
                descricao='Descrição da aula sobre Reflexão.'
            )
        elif subtopico == 'Centro de massa':
            pagina_subtopico(
                titulo='Centro de massa',
                video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                material_url='https://example.com/refracao.pdf',
                descricao='Descrição da aula sobre Refração.'
            )

# Configurações do Streamlit
st.set_page_config(page_title='Física a Nível Militar', layout='wide')

# Verifica se o usuário está logado
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if st.session_state['logado']:
    menu_topicos()
else:
    pagina_login()

# Rodapé
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("© 2024 Física a Nível Militar. Todos os direitos reservados.", unsafe_allow_html=True)
