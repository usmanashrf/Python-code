with open(r"C:\\Users\\haieer\\Documents\\DevC++ codes\\1stWeb & E-commerce.txt","r+")as input:

   File  = input.read()
    with open(r"C:\\Users\\haieer\\Desktop\2ndWeb & E-commerce.txt", "w+")as input:
     input.writelines(str(File).replace(",","").replace("Pakistan",",").replace("PKR",",PKR").replace("USD",",USD").replace("ALL",",ALL").replace("GBP",",GBP").replace("EUR",",EUR").replace("AED",",AED").replace("PAB",",PAB").replace("SAR",",SAR").replace("AFN",",AFN").replace("CAD",",CAD").replace("JPY",",JPY"))
    input.close
