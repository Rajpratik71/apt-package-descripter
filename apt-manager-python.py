import apt_pkg

apt_pkg.init()
mycache = apt_pkg.Cache()
mydepcache = apt_pkg.DepCache(mycache)

pkgname = input("Enter the package name: ")
pkgver = mydepcache.get_candidate_ver(mycache[pkgname])
print("The given package version is : ", pkgver)
