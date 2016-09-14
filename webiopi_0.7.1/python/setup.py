from setuptools import setup, Extension

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: Apache Software License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(name             = 'WebIOPi',
      version          = '0.7.1',
      author           = 'Eric PTAK',
      author_email     = 'trouch@trouch.com',
      description      = 'A package to control Raspberry Pi GPIO from the web',
      long_description = open('../doc/README').read(),
      license          = 'Apache',
      keywords         = 'RaspberryPi GPIO Python REST',
      url              = 'http://webiopi.trouch.com/',
      classifiers      = classifiers,
      packages         = ['_webiopi',
                          "webiopi",
                          "webiopi.utils",
                          "webiopi.clients",
                          "webiopi.protocols",
                          "webiopi.server",
                          "webiopi.decorators",
                          "webiopi.devices",
                          "webiopi.devices.digital",
                          "webiopi.devices.analog",
                          "webiopi.devices.sensor",
                          "webiopi.devices.clock", 
			  "webiopi.devices.memory", 
			  "webiopi.devices.shield"
                          ],
      ext_modules      = [Extension(name='_webiopi.GPIO', sources=['native/bridge.c', 'native/gpio.c', 'native/cpuinfo.c'], include_dirs=['native/'])],
      headers          = ['native/cpuinfo.h', 'native/gpio.h'],   
      )
