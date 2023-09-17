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

        # Determinar el número de tokens permitidos en función de la edad
        if edad <= 5:
            max_tokens = 800
        elif edad <= 8:
            max_tokens = 1200
        elif edad <= 10:
            max_tokens = 1600
        else:
            max_tokens = 2000

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=max_tokens,
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

            # Descargar el cuento generado como archivo
            if st.button("Descargar"):
                with open(f"cuento_para_ninos_{edad_opcion.replace(' ', '_')}.txt", "w") as file:
                    file.write(cuento)
                st.success("¡El cuento se ha descargado exitosamente!")

    # Ejecutar la aplicación
    if __name__ == '__main__':
        main()
