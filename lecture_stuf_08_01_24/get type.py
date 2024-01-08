def get_type(value):

    match (type(value).__name__):
        case "int":
            return "Integer"
        case "float":
            return "Float"
        case "str":
            return "String"
        case "list":
            return "List"
        case "dict":
            return "Dictionary"
        case "tuple":
            return "Tuple"
        case _:
            return "unknown type"
        
print(get_type(3.14)) #Output:Float