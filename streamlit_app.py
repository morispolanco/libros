import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Ingresa tu clave de API de OpenAI", type="password")

if not api_key:
    st.warning("Por favor, ingresa una clave de API válida para continuar.")
else:
    openai.api_key = api_key

    # Función para generar cuentos utilizando GPT-3
    def generar_cuento(edad):
        prompt = f"Genera un cuento para niños de {edad} años.\n\n"

        # Obtener el valor de la edad
        edad = edad[0]

        # Determinar el número de palabras permitidas en función de la edad
        num_palabras = 300 + (edad - 3) * 200

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=num_palabras,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=10
        )
        return response.choices[0].text.strip()

    # Función principal de la aplicación
    def main():
        st.title("Generador de Cuentos para Niños")
        st.write("¡Bienvenido! Utiliza este generador para crear cuentos para niños en español.")

        # Opciones de rangos de edad
        opciones_edad = {
            "De 3 a 5 años": (3, 5),
            "De 6 a 8 años": (6, 8),
            "De 9 a 10 años": (9, 10),
            "De 11 a 15 años": (11, 15)
        }

        # Obtener el rango de edad seleccionado
        edad_opcion = st.selectbox("Selecciona el rango de edad", list(opciones_edad.keys()))

        # Generar el cuento
        if st.button("Generar Cuento"):
            rango_edad = opciones_edad[edad_opcion]
            cuento = generar_cuento(rango_edad)

            # Mostrar el cuento generado
            st.subheader("Cuento generado:")
            st.write(cuento)

    # Ejecutar la aplicación
    if __name__ == '__main__':
        main()
