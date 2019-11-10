import os
import os.path
import configparser


def read_save_file():
    path_ini = configparser.ConfigParser()
    path_ini.read('Savefiles/path.ini')
    return path_ini


def read_ta_system():
    system_ini = configparser.ConfigParser()
    system_ini.read(path)
    return system_ini


path = os.path.expanduser(read_save_file().get('SaveFiles', 'tasystempath'))


def open_game():
    path_to_game = read_save_file().get('SaveFiles', 'PathToGame')
    try:
        if os.path.isfile(path_to_game):
            os.system(path_to_game)
            return False
        return True
    except KeyError:
        return


def set_size(size):
    config = read_ta_system()
    try:
        config.set('SystemSettings', 'Fullscreen', 'False')
        config.set('SystemSettings', 'Borderless', 'True')
        if size == 'big':
            config.set('SystemSettings', 'ResX', '3840')
        else:
            config.set('SystemSettings', 'ResX', '1920')

        with open(path, 'w') as configfile:
            config.write(configfile)
        return True
    except KeyError:
        print("Something went wrong")
        return False


def set_path_setting(configuration, setting, value):
    config = read_save_file()
    try:
        config.set(configuration, setting, value)
        with open('Savefiles/path.ini', 'w') as configfile:
            config.write(configfile)
    except KeyError:
        print("Something went wrong")


def get_path():
    return path


def get_size():
    config = read_ta_system()
    return config.get('SystemSettings', 'ResX')


def is_fps_improved():
    config = read_ta_system()
    if (config.get('SystemSettings', 'AllowPerFrameSleep') == 'False'
            and config.get('SystemSettings', 'AllowPerFrameYield') == 'False'
            and config.get('SystemSettings', 'StaticDecals') == 'False'
            and config.get('SystemSettings', 'DecalCullDistanceScale') == '0.500000'
            and config.get('SystemSettings', 'DynamicLights') == 'False'
            and config.get('SystemSettings', 'DynamicShadows') == 'False'
            and config.get('SystemSettings', 'LightEnvironmentShadows') == 'False'
            and config.get('SystemSettings', 'CompositeDynamicLights') == 'False'):
        return True
    else:
        return False


def improve_fps():
    config = read_ta_system()
    config.set('SystemSettings', 'AllowPerFrameSleep', 'False')
    config.set('SystemSettings', 'AllowPerFrameYield', 'False')
    config.set('SystemSettings', 'StaticDecals', 'False')
    config.set('SystemSettings', 'DecalCullDistanceScale', '0.500000')
    config.set('SystemSettings', 'DynamicLights', 'False')
    config.set('SystemSettings', 'DynamicShadows', 'False')
    config.set('SystemSettings', 'LightEnvironmentShadows', 'False')
    config.set('SystemSettings', 'CompositeDynamicLights', 'False')
    config.set('SystemSettings', 'SHSecondaryLighting', 'False')
    config.set('SystemSettings', 'MotionBlur', 'False')
    config.set('SystemSettings', 'MotionBlurPause', 'False')
    config.set('SystemSettings', 'MotionBlurSkinning', '0')
    config.set('SystemSettings', 'DepthOfField', 'True')
    config.set('SystemSettings', 'AmbientOcclusion', 'False')
    config.set('SystemSettings', 'Distortion', 'False')
    config.set('SystemSettings', 'FilteredDistortion', 'False')
    config.set('SystemSettings', 'DropParticleDistortion', 'True')
    config.set('SystemSettings', 'LensFlares', 'False')
    config.set('SystemSettings', 'OneFrameThreadLag', 'False')
    config.set('SystemSettings', 'AllowRadialBlur', 'False')
    config.set('SystemSettings', 'AllowSubsurfaceScattering', 'False')
    config.set('SystemSettings', 'AllowImageReflectionShadowing', 'False')
    config.set('SystemSettings', 'MaxFilterBlurSampleCount', '2')
    config.set('SystemSettings', 'DetailMode', '0')
    config.set('SystemSettings', 'AllowApexCloth', 'False')
    config.set('SystemSettings', 'bEnableForegroundShadowsOnWorld', 'False')
    config.set('SystemSettings', 'bAllowFracturedDamage', 'False')

    with open(path, 'w') as configfile:
        config.write(configfile)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
