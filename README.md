# Python ile eviniz akıllı olsun
Python İstanbul topluluğu için Python Saati #44 etkinliğinde yaptığım sunum. Tüm katılımcılara teşekkürler!

## Sunum
[RISE](https://github.com/damianavila/RISE) kullanılarak hazırlandı. Yüklemek için:

```
pip install RISE
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

Çalıştırmak için:

```
jupyter notebook
```

GIF'leri görüntüleyebilmek için static klasöründe:

```
python -m SimpleHTTPServer
```

## Home Assistant bileşeni

Bileşen klasöründeki `weasley_clock.py` dosyasını `~/.homeassistant/custom_components/` dizini içerisine kopyalayıp Home Assistant'ı yeniden başlatın.

## Weasley Saati uygulaması

`weasley-clock` klasöründeki uygulamayı bağımlılıklarını yükledikten sonra çalıştırın.

## Weasley Saati baskısı

Saati 3B yazıcı ile basmak için gerekli tasarımlar: https://www.thingiverse.com/onurguzel/collections/weasley-clock

---

## Make you home smarter with Python

This is the presentation I made at Python Hour #44 event for Python Istanbul community. The slides are in Turkish.
