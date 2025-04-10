# -*- coding: utf-8 -*-
import re # Importamos el módulo de expresiones regulares

# === INPUT ===
# Pega aquí tu string multilínea con los datos originales
input_data_string = """
 - [811.30200000000002, 499.47199999999998, 0, ""]
      - [757.34199999999998, 332.69799999999998, 0, ""]
      - [901.60900000000004, 333.93299999999999, 0, ""]
      - [923.29899999999998, 333.93299999999999, 0, ""]
      - [923.29899999999998, 328.19799999999998, 0, ""]
      - [1034.8030000000001, 390.21100000000001, 0, ""]
      - [969.84500000000003, 425.49400000000003, 0, ""]
      - [975.61400000000003, 424.17399999999998, 0, ""]
      - [983.07500000000005, 437.88600000000002, 0, ""]
      - [1000.798, 467.70800000000003, 0, ""]
      - [1026.3699999999999, 514.32600000000002, 0, ""]
      - [1011.0940000000001, 484.88999999999999, 0, ""]
      - [1070.104, 449.76999999999998, 0, ""]
      - [1068.883, 328.19799999999998, 0, ""]
      - [1068.883, 333.77999999999997, 0, ""]
      - [1089.0519999999999, 333.77999999999997, 0, ""]
      - [1089.0519999999999, 327.91500000000002, 0, ""]
      - [1234.8219999999999, 327.91500000000002, 0, ""]
      - [1234.8219999999999, 333.73200000000003, 0, ""]
      - [1256.5440000000001, 333.73200000000003, 0, ""]
      - [1256.5440000000001, 325.58600000000001, 0, ""]
      - [1401.6179999999999, 325.58600000000001, 0, ""]
      - [1401.6179999999999, 332.56799999999998, 0, ""]
      - [1422.953, 332.56799999999998, 0, ""]
      - [1422.953, 313.94900000000001, 0, ""]
      - [1417.925, 313.94900000000001, 0, ""]
      - [1419.97, 294.14400000000001, 0, ""]
      - [1427.77, 270.02100000000002, 0, ""]
      - [1437.5709999999999, 246.14400000000001, 0, ""]
      - [1450.3130000000001, 227.19499999999999, 0, ""]
      - [1467.3009999999999, 208.24600000000001, 0, ""]
      - [1483.6369999999999, 194.524, 0, ""]
      - [1500.625, 183.09, 0, ""]
      - [1520.2280000000001, 173.61500000000001, 0, ""]
      - [1540.623, 167.81399999999999, 0, ""]
      - [1559.203, 164.30600000000001, 0, ""]
      - [1575.183, 163.39699999999999, 0, ""]
      - [1589.2149999999999, 162.87700000000001, 0, ""]
      - [1601.8320000000001, 163.67599999999999, 0, ""]
      - [1615.7670000000001, 165.62700000000001, 0, ""]
      - [1630.816, 170.78200000000001, 0, ""]
      - [1643.915, 175.79900000000001, 0, ""]
      - [1655.1310000000001, 182.37899999999999, 0, ""]
      - [1665.568, 188.38200000000001, 0, ""]
      - [1676.2819999999999, 195.95599999999999, 0, ""]
      - [1685.6099999999999, 204.54499999999999, 0, ""]
      - [1694.107, 212.858, 0, ""]
      - [1703.6210000000001, 223.11000000000001, 0, ""]
      - [1711.769, 234.16300000000001, 0, ""]
      - [1718.617, 246.738, 0, ""]
      - [1724.8420000000001, 259.06400000000002, 0, ""]
      - [1729.6980000000001, 270.76799999999997, 0, ""]
      - [1734.2180000000001, 284.911, 0, ""]
      - [1737.1880000000001, 297.78500000000003, 0, ""]
      - [1738.1790000000001, 311.97899999999998, 0, ""]
      - [1738.8389999999999, 322.322, 0, ""]
      - [1738.1890000000001, 339.38400000000001, 0, ""]
      - [1736.356, 353.56099999999998, 0, ""]
      - [1732.548, 367.15600000000001, 0, ""]
      - [1728.0319999999999, 382.73200000000003, 0, ""]
      - [1721.559, 395.22399999999999, 0, ""]
      - [1713.7329999999999, 409.63999999999999, 0, ""]
      - [1703.23, 424.88, 0, ""]
      - [1692.367, 436.12900000000002, 0, ""]
      - [1680.2539999999999, 447.89400000000001, 0, ""]
"""

# === PARÁMETROS DE TRANSFORMACIÓN ===
center_x = 15.891
center_y = -111.593
scale = 1.022 # Escala uniforme para x e y

# === PROCESAMIENTO ===
output_lines = [] # Lista para guardar las líneas procesadas

# Expresión regular para encontrar las líneas de coordenadas y capturar partes
# Grupo 1: Prefijo (espacios y guion)
# Grupo 2: Valor X (string)
# Grupo 3: Valor Y (string)
# Grupo 4: Parte Z (string, ej: " 0")
# Grupo 5: Parte Label (string, ej: ' ""') - Mantenemos el espacio y las comillas
coord_pattern = re.compile(r"(\s*-\s*)\[\s*([^,]+)\s*,\s*([^,]+)\s*,(.*),(.*\")\s*\]")

# Dividimos el string de entrada en líneas y procesamos cada una
for line in input_data_string.strip().split('\n'):
    match = coord_pattern.match(line)
    if match:
        # Si la línea coincide con el patrón de coordenadas
        prefix = match.group(1) # Captura la indentación y el guion
        x_str = match.group(2).strip()
        y_str = match.group(3).strip()
        z_part = match.group(4).strip() # Captura la parte Z como string
        label_part = match.group(5).strip() # Captura la parte de la etiqueta como string (con comillas)

        try:
            # Convierte las coordenadas x, y a números flotantes
            x = float(x_str)
            y = float(y_str)

            # Aplica la fórmula de transformación
            transformed_x = ((x - center_x) * scale) + center_x
            transformed_y = ((y - center_y) * scale) + center_y

            # Reconstruye la línea con los valores transformados y el formato original
            # Usamos los z_part y label_part originales para mantener el formato exacto
            new_line = f"{prefix}[{transformed_x}, {transformed_y}, {z_part}, {label_part}]"
            output_lines.append(new_line)

        except ValueError:
            # Si la conversión a float falla, añade la línea original (poco probable con este regex)
            output_lines.append(line)
            print(f"Advertencia: No se pudieron convertir coordenadas en la línea: {line}")

    else:
        # Si la línea no coincide (ej. línea vacía, comentario), la añadimos tal cual
        if line.strip(): # Evita añadir líneas completamente vacías si las hubiera
             output_lines.append(line)

# === SALIDA ===
# Unimos las líneas procesadas de nuevo en un solo string
output_string = "\n".join(output_lines)

# Imprimimos el resultado final
print("--- Coordenadas Transformadas (String Output) ---")
print(output_string)
print("--- Fin ---")