def linearSearchProduct (productList, targetProduct): 
    indices = []

    for index,products in enumerate(productList):
      if products==targetProduct:
        indices.append(index)
    
    return indices 


#Example usage :
products = ["shoes", "boot", "loafer", "shoes", "sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)