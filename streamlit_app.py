import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Ingresa tu clave de API de OpenAI", type="password")

if not api_key:
    st.warning("Por favor, ingresa una clave de API válida para continuar.")
else:
    openai.api_key = api_key

    # Función para generar texto utilizando GPT-3
    def generar_texto(titulo, numero_capitulo):
        prompt = f"Capítulo {numero_capitulo}: {titulo}\n\n"

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

    # Función principal de la aplicación
    def main():
        st.title("Generador de Libros con GPT-3")
        st.write("¡Bienvenido! Utiliza este generador para escribir un libro con la ayuda de GPT-3.")

        # Obtener el título del libro
        titulo = st.text_input("Ingresa el título del libro")

        # Obtener el número del capítulo
        numero_capitulo = st.number_input("Ingresa el número del capítulo", min_value=1, step=1)

        # Generar el texto del libro
        if st.button("Generar"):
            if titulo:
                contenido_libro = generar_texto(titulo, numero_capitulo)

                # Mostrar el texto generado
                st.subheader("Texto generado:")
                st.write(contenido_libro)

                # Descargar el texto generado como archivo
                if st.button("Descargar"):
                    with open(f"{titulo}_capitulo{numero_capitulo}.txt", "w") as file:
                        file.write(contenido_libro)
                    st.success("¡El archivo se ha descargado exitosamente!")
            else:
                st.warning("Por favor, ingresa un título para el libro.")

    # Ejecutar la aplicación
    if __name__ == '__main__':
        main()
