l1 = ["ima","sar","nago"]
l2 = ["ap1","ap2","ap3"]

with open ("nombres_apellidos.txt","w") as arch:
    arch.writelines("Los nombres con sus correspondientes apellidos serían : \n\n")
    [arch.writelines(f"Nombre : {n}\nApellido : {a}\n ------------------- \n") for n,a in zip(l1,l2)]