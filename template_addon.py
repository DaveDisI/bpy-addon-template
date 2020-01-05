import bpy

bl_info = {
    "name": "Property Example", #CHANGE THIS
    "blender": (2, 80, 0),
    "category": "Object",
}

      #CHANGE THIS
class ExampleClass(bpy.types.Operator):
    bl_idname = "object.property_example"  #CHANGE THIS
    bl_label = "Property Example" #CHANGE THIS
    bl_options = {'REGISTER', 'UNDO'}

    my_float: bpy.props.FloatProperty(name="Some Floating Point") #CHANGE THIS
    my_bool: bpy.props.BoolProperty(name="Toggle Option") #CHANGE THIS
    my_string: bpy.props.StringProperty(name="String Value") #CHANGE THIS

    def execute(self, context): #CODE TO RUN WHEN EXECUTED
        if self.my_string is '':
            return {'FINISHED'}
        print('My float:', self.my_float)
        print('My bool:', self.my_bool)
        print('My string:', self.my_string)
        return {'FINISHED'}

def menu_func(self, context): 
    self.layout.operator(ExampleClass.bl_idname)

def register():
    bpy.utils.register_class(ExampleClass) #CHANGE THIS
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(ExampleClass) #CHANGE THIS
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
if __name__ == "__main__":
    register()
