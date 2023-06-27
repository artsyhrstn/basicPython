# Tipe Data

# a = 10, a adalah variabel dengan nilai 10

# 1. Integer = Angka Satuan
data_integer = 1
print("data :", data_integer, ", bertipe", type(data_integer))

# 2. Float = Angka Desimal, dengan koma
data_float = 1.5
print("data : ", data_float)
print("- tipe data :", type(data_float))

# 3. String = Kumpulan Karakter
data_string = "buku" # Memasukan nilai string harus menggunakan tanda petik
print ("data :", data_string)
print ("- tipe data", type (data_string)) #menginput variabel harus menggunakan tanda kurung

# 4. Binary = true/false (boolean)
data_bool = True # Hanya bisa true / false
print ("data", data_bool)
print ("- tipe data", type (data_bool))

# Tipe data Khusus
# 1. Bilangan Kompleks
data_kompleks = complex(5, 6) # depan ditaroh untuk bilangan riil, sedangkan belakang untuk bilangan imajiner
print ("data", data_kompleks)
print ("- tipe data", type (data_kompleks))

# 2. Bilangan dari Bahasa C
from ctypes import c_double, c_char #untuk mengakomodasi jagoan c

data_c_double = c_double(10,5)
print ("data", data_c_double)
print ("- tipe data", type (data_c_double))
# Belum Sampe C wado



