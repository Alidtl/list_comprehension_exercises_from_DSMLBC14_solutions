#####################################################################################################################
# Görev 1:  List Comprehension yapısıkullanarakcar_crashesverisindekinumeric değişkenlerinisimlerini büyük harfe
# çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
print([("NUM_" + col.upper()) if df[col].dtype != "O" else col.upper() for col in df.columns])

#####################################################################################################################

# Görev 2:  List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin
# isimlerinin sonuna "FLAG" yazınız.

print([(col.upper() + "_FLAG") if "no" not in col else col.upper() for col in df.columns])

#####################################################################################################################

# Görev 3:  List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin
# isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]

print(new_df)

#####################################################################################################################
