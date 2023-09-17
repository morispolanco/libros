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
            max_tokens=4000,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=10
        )
        return response.choices[0].text.strip()

    # Función para guardar el texto generado en un archivo .txt
    def guardar_texto_en_archivo(texto_generado):
        with open("libro_generado.txt", "w") as archivo:
            archivo.write(texto_generado)

    # Función principal de la aplicación
    def main():
        st.title("Generador de Libros con GPT-3")
        st.write("¡Bienvenido! Utiliza este generador para escribir un libro con la ayuda de GPT-3.")

        # Obtener el título del libro
        titulo = st.text_input("Ingresa el título del libro")

        # Obtener el número de capítulos
        num_capitulos = st.number_input("Ingresa el número de capítulos", min_value=1, step=1)

        # Obtener el número de palabras por capítulo
        num_palabras_por_capitulo = st.number_input("Ingresa el número de palabras por capítulo", min_value=1, step=1, max_value=4000)

        # Obtener la audiencia a la que va dirigido el libro
        audiencia = st.selectbox("Selecciona la audiencia a la que va dirigido el libro", ["Niños", "Adolescentes", "Adultos"])

        # Generar el texto del libro
        if st.button("Generar"):
            if titulo and num_capitulos and num_palabras_por_capitulo and audiencia:
                prompt = f"#{titulo}\n\nEste libro consta de {num_capitulos} capítulos, cada uno con aproximadamente {num_palabras_por_capitulo} palabras. Está dirigido a {audiencia}.\n\n"

                # Generar el contenido de cada capítulo
                contenido_capitulos = []
                for i in range(num_capitulos):
                    contenido_capitulo = generar_texto(f"Capítulo {i+1}\n\n")
                    contenido_capitulos.append(contenido_capitulo)

                # Combinar el contenido de cada capítulo en el texto completo del libro
                texto_generado = prompt + "\n\n".join(contenido_capitulos)
                st.subheader("Texto generado:")
                st.write(texto_generado)

                # Guardar el texto generado en un archivo .txt
                guardar_texto_en_archivo(texto_generado)

                # Proporcionar un enlace de descarga al usuario
                st.markdown("[Descargar libro generado](libro_generado.txt)")
            else:
                st.warning("Por favor, completa todos los campos.")

    # Ejecutar la aplicación
    if __name__ == '__main__':
        main()
