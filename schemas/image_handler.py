
image_handler_types ="""
    scalar Upload

    type image {
    image: Upload
    }

"""
image_handler_query = """
"""
image_handler_mutation = """
    uploadImage(image: Upload!): [image]
"""