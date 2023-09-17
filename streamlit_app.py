import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Ingresa tu clave de API de OpenAI", type="password")

if not api_key:
    st.warning("Por favor, ingresa una clave de API válida para continuar.")
else:
    openai.api_key = api_key

    # Función para generar texto utilizando GPT-3
    def generar_texto(prompt):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=4096,  # Utilizar el máximo número de tokens posible
            temperature=0.7,
            n=1,
            stop=None,
            timeout=10
        )
        return response.choices[0].text.strip()

    # Función principal de la aplicación
    def main():
        st.title("Generador de Libros con GPT-3")
        st.write("¡Bienvenido! Utiliza este generador para escribir un libro con la ayuda de GPT-3.")

        # Obtener el título del libro
        titulo = st.text_input("Ingresa el título del libro")

        # Obtener el texto inicial del libro
        texto_inicial = st.text_area("Ingresa el texto inicial del libro")

        # Generar el texto del libro
        if st.button("Generar"):
            if titulo and texto_inicial:
                prompt = f"#{titulo}\n\n{texto_inicial}\n\n"
                texto_generado = generar_texto(prompt)
                st.subheader("Texto generado:")
                st.write(texto_generado)
            else:
                st.warning("Por favor, ingresa el título y el texto inicial del libro.")

    # Ejecutar la aplicación
    if __name__ == '__main__':
        main()
