from datatypes import *
from PIL import Image

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls
    
@deco(BuiltInFunction)
def execute_load_img(self, exec_ctx):
    path = exec_ctx.symbol_table.get('path')
    if not isinstance(path, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
        ))
    image_path = path.value
    try:
        image = Image.open(image_path)
    except:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "image not found!",
            exec_ctx
        ))
    rgb_image = image.convert("RGB")
    width, height = rgb_image.size
    rgb_list: List(List(List(Number))) = List([List([List([Number(0), Number(0), Number(0)]) for _ in range(width)]) for _ in range(height)])
    for y in range(height):
        for x in range(width):
            pixel = list(rgb_image.getpixel((x, y)))
            rgb_list.elements[y].elements[x] = List(pixel)

    return RTResult().success(rgb_list)

BuiltInFunction.execute_load_img.arg_names = ['path']
BuiltInFunction.execute_load_img.infinite = False
BuiltInFunction.execute_load_img.accept_none = False

@deco(BuiltInFunction)
def execute_save_img(self, exec_ctx):
    rgblist = exec_ctx.symbol_table.get('list')
    output_path = exec_ctx.symbol_table.get('path').value
    if not isinstance(rgblist, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "first argument must be a 3d array",
            exec_ctx
        ))
    rgb_list = rgblist.elements
    if isinstance(rgb_list[0], list):
        width = len(List(rgb_list[0]).elements)
    else:
        width = len(rgb_list[0].elements)
    height = len(rgb_list)
    image = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            if isinstance(rgb_list[0], List):
                pixel = rgb_list[y].elements[x]
                if isinstance(pixel.elements[0], Number):
                    image.putpixel((x, y), tuple(z.value for z in pixel.elements))
                else:
                    image.putpixel((x, y), tuple(z for z in pixel.elements))
            else:
                pixel = rgb_list[y][x]
                image.putpixel((x, y), tuple(pixel))
        # حفظ_صورة([[[0,0,0], [0,0,0]],[[0,0,0], [0,0,0]]], "بلابلابلا.png")
    image.save(output_path)

    return RTResult().success(List(rgb_list))

BuiltInFunction.execute_save_img.arg_names = ['list', 'path']
BuiltInFunction.execute_save_img.infinite = False
BuiltInFunction.execute_save_img.accept_none = False

BuiltInFunction.load_img = BuiltInFunction("load_img")
BuiltInFunction.save_img = BuiltInFunction("save_img")

global_symbol_table.set(f"{data_dict['load']}", BuiltInFunction.load_img)
global_symbol_table.set(f"{data_dict['save_img']}", BuiltInFunction.save_img)