* D:\software_install\Qt\Qt5.12.7\5.12.7\msvc2017_64\bin
or C:\Users\yhw-miracle\Documents\workspace_FreeCAD\FreeCADLibs_12.1.4_x64_VC15\bin

pyside2-lupdate.exe
lupdate.exe
linguist.exe
lrelease.exe

* ready
```python
def QT_TRANSLATE_NOOP(context, text):
    return text

from PySide.QtCore import QT_TRANSLATE_NOOP
```

* lupdate *.ui -ts translations/uifiles.ts

* pylupdate5 *.py -ts translations/pyfiles.ts

* 生成源 ts 文件
lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/BIM.ts

* 生成其他语言 ts 文件
```python
import sys 
import os
import shutil


if __name__ == "__main__":
    modulename = "A2plus" # the name of your module
    translations = "translations" # the path to the translations files location, inside your module folder
    languages = "af ar ca cs de el es-ES eu fi fil fr gl hr hu id it ja kab ko lt nl no pl pt-BR pt-PT ro ru sk sl sr sv-SE tr uk val-ES vi zh-CN zh-TW"

    for lncode in languages.split(" "):
        tsfilepath = os.path.join(os.path.dirname(__file__),modulename+".ts")
        newtspath = os.path.join(os.path.dirname(__file__),modulename+"_"+lncode+".ts")
        newqmpath = os.path.join(os.path.dirname(__file__),modulename+"_"+lncode+".qm")
        print(tsfilepath)
        print(newtspath)
        shutil.copyfile(tsfilepath, newtspath)
        os.system("lrelease " + newtspath)
        if not os.path.exists(newqmpath):
            print("ERROR: unable to create", newqmpath, ", aborting")
            sys.exit()
```

* 翻译
linguist.exe 打开 对应语言的 ts 文件

* 编译 ts 文件
```python
import os


if __name__ == "__main__":
    modulename = "A2plus" # the name of your module
    translations = "translations" # the path to the translations files location, inside your module folder
    languages = "af ar ca cs de el es-ES eu fi fil fr gl hr hu id it ja kab ko lt nl no pl pt-BR pt-PT ro ru sk sl sr sv-SE tr uk val-ES vi zh-CN zh-TW"

    for lncode in languages.split(" "):
        newtspath = os.path.join(os.path.dirname(__file__),modulename+"_"+lncode+".ts")
        newqmpath = os.path.join(os.path.dirname(__file__),modulename+"_"+lncode+".qm")
        os.system("lrelease " + newtspath)
        if not os.path.exists(newqmpath):
            print("ERROR: unable to create", newqmpath, ", aborting")
            sys.exit()

```

* A2plus CMakeLists.txt
```txt
IF (BUILD_GUI)
	PYSIDE_WRAP_RC(A2plus_QRC_SRCS A2plus.qrc)
ENDIF (BUILD_GUI)

SET(A2plus_SRCS
    a2plib.py
	a2p_bom.py
	a2p_constraintcommands.py
	a2p_constraintDialog.py
	a2p_constraints.py
	a2p_constraintServices.py
	a2p_convertPart.py
	a2p_dependencies.py
	a2p_fcdocumentreader.py
	a2p_importedPart_class.py
	a2p_importpart.py
	a2p_lcs_support.py
	a2p_libDOF.py
	a2p_MuxAssembly.py
	a2p_observers.py
	a2p_partinformation.py
	a2p_partlistglobals.py
	a2p_recursiveUpdatePlanner.py
	a2p_Resources2.py
	a2p_Resources3.py
	a2p_rigid.py
	a2p_searchConstraintConflicts.py
	a2p_simpleXMLreader.py
	a2p_solversystem.py
	a2p_topomapper.py
	a2p_versionmanagement.py
	a2p_viewProviderProxies.py
	compileA2pResources.py
	Init.py
	InitGui.py
)

SOURCE_GROUP("" FILES ${A2plus_SRCS})

SET(A2plusGuiIcon_SVG
	icons/a2p_Workbench.svg
)

ADD_CUSTOM_TARGET(A2plus ALL
	SOURCES ${A2plus_SRCS} ${A2plus_QRC_SRCS} ${A2plusGuiIcon_SVG}
)

fc_copy_sources(A2plus "${CMAKE_BINARY_DIR}/Mod/A2plus" ${A2plus_SRCS})
fc_copy_sources(A2plus "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_DATADIR}/Mod/A2plus" ${A2plusGuiIcon_SVG})

IF (BUILD_GUI)
	fc_target_copy_resource(A2plus
		${CMAKE_CURRENT_BINARY_DIR}
		${CMAKE_BINARY_DIR}/Mod/A2plus
		A2plus_rc.py)
ENDIF (BUILD_GUI)

INSTALL(
	FILES
		${A2plus_SRCS}
		${A2plus_QRC_SRCS}
	DESTINATION Mod/A2plus
)
```