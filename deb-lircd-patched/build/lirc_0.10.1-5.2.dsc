-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Format: 3.0 (quilt)
Source: lirc
Binary: lirc, lirc-doc, liblirc0, liblircclient0, liblircclient-dev, liblirc-dev, liblirc-client0, lirc-x
Architecture: any all
Version: 0.10.1-5.2
Maintainer: Debian Lirc Team <team+debian-lirc@tracker.debian.org>
Uploaders:  Stefan Lippers-Hollmann <s.l-h@gmx.de>, Alec Leamas <leamas.alec@gmail.com>
Homepage: https://sf.net/p/lirc
Standards-Version: 4.3.0
Vcs-Browser: https://gitlab.com/leamas/lirc
Vcs-Git: https://gitlab.com/leamas/lirc.git
Build-Depends: debhelper (>= 11), dh-exec, dh-python, doxygen, expect [!hurd-any], kmod [linux-any], libasound2-dev [linux-any kfreebsd-any], libftdi1-dev, libsystemd-dev [linux-any], libudev-dev [linux-any], libusb-1.0-0-dev [!kfreebsd-any], libusb-dev [!kfreebsd-any], libx11-dev, man2html-base, pkg-config, portaudio19-dev, python3-dev (>= 3.5), python3-setuptools, python3-yaml, socat [!hurd-any], systemd [linux-any], xsltproc
Package-List:
 liblirc-client0 deb libs optional arch=any
 liblirc-dev deb libdevel optional arch=any
 liblirc0 deb libs optional arch=any
 liblircclient-dev deb libdevel optional arch=any
 liblircclient0 deb libs optional arch=any
 lirc deb utils optional arch=any
 lirc-doc deb doc optional arch=all
 lirc-x deb utils optional arch=any
Checksums-Sha1:
 0188b9886d3bd0d4f0819050865001e2dc7e85e3 2715271 lirc_0.10.1.orig.tar.gz
 e930a028201f4e026a490fc96e3c094ff811c6cd 35876 lirc_0.10.1-5.2.debian.tar.xz
Checksums-Sha256:
 25b0a5c761d927e9651e6eb54d0ce4cce3870ebb893afad5c4b181182fc642c1 2715271 lirc_0.10.1.orig.tar.gz
 ef2dcc608e63baf20fe5df9ebe82ee98ea0526730e5001916dfb112fc399387a 35876 lirc_0.10.1-5.2.debian.tar.xz
Files:
 2a390b353181fe6c6b5b94dcd10ba743 2715271 lirc_0.10.1.orig.tar.gz
 5c33ee654207b8b938967652720479e2 35876 lirc_0.10.1-5.2.debian.tar.xz

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEE/d0M/zhkJ3YwohhskWT6HRe9XTYFAlyopgAACgkQkWT6HRe9
XTYqOg//RbDlqbeiXb1ta3po3tVGmqo3+3hDTnW98JX6QjBdlwHphJ3Upb5//axt
I4j8ZF+pdM245JR17IA4yNXqNrA3/ZxxfSiUj02wN6eNwvC94XbBzJACIKoOLpSl
pDcgw37JAw7geImpGcuQvJhBCX7h3Ma59vT/33P+qaRT/7l/WrOZlhP1j6qqFaYP
ZaQq413ikKKG1dPdecyPH2Gp4iCkwPwVZ4E7JxUe8UjzeGmNud2ix/FW3Dr3ELKa
xML+hoU24/FHbo0G9pyOrrUOPUv/eQfl/L2i7lQWSYv58PLzq10ixr4f45Bzfr4J
rQXxqra4KlsrIJhmnAslHMyVeB7mOmAGgKLFDmQxjKvMKUe2wSCjtr8YU6Rs4ZTU
PxUpDgMSACtx5PPewCX9oEcAkeJfABpAPNQXv3R8UzfOGO6oVFHFAdk6OL2k37ss
5wba4w2HEF1cG7k97cofxaeWEdE5iZhLPajwo4Vu6Eo0XSKTE+d561fzoFmvpC1d
rffv8cg/3nKhATGYOPxat//5pna0X+0jtIimgu7mAHtXmaTdA6b59iQtrumHCrTj
F21XC40vG3gslcM1A8ZuunjFOqbz4JJXLxqtgolS2Lwo000xRUxL5VooGfMB7ill
MhfW9ruRgKWCzfMdinCx33kjrXjZ14Ee9YvPi7iRd7FivaFqvS8=
=FAON
-----END PGP SIGNATURE-----
