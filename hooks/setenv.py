import os
import zc.buildout


os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'


def appendEnvVar(env,var,sep=":",before=True):
    """ append text to a environnement variable
    @param env String variable to set
    @param before append before or after the variable"""
    for path in var:
    	if before:os.environ[env] = "%s%s%s" % (path,sep,os.environ.get(env,''))
	else:os.environ[env] = "%s%s%s" % (os.environ.get(env,''),sep,path)


def getpostgresqlenv(options,buildout):
    for var in ['python','readline','ncurses','openssl','openldap','zlib']:
        appendEnvVar('LDFLAGS',         ["-L%(lib)s/lib -Wl,-rpath -Wl,%(lib)s/lib %(os)s"%{'lib':buildout[var]['location'],'os':os_ldflags}],sep=' ',before=False)
        appendEnvVar('EXTRA_LDAP_LIBS', ["-L%(lib)s/lib -Wl,-rpath -Wl,%(lib)s/lib %(os)s"%{'lib':buildout[var]['location'],'os':os_ldflags}],sep=' ',before=False)
        appendEnvVar('LIBS', ["-L%(lib)s/lib -Wl,-rpath -Wl,%(lib)s/lib"%{'lib':buildout[var]['location']}],sep=' ',before=False)
        appendEnvVar('LD_RUN_PATH', ["%(lib)s/lib"%{'lib':buildout[var]['location']}],sep=':',before=False)
        appendEnvVar('CFLAGS',   ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
        appendEnvVar('CPPFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
        appendEnvVar('CXXFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
    appendEnvVar('CFLAGS', ["-I%s/include/openssl "%(buildout['openssl']['location'])],sep=' ',before=False)
    os.environ['CPPFLAGS'] = os.environ['CFLAGS']
    os.environ['CXXFLAGS'] = os.environ['CFLAGS']


# vim:set ts=4 sts=4 et  :
