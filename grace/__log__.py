
{'date': 'Sun Mar 10 2024 11:45:01.385 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 8
    STYLE.update(height="500px", width="500px")
AttributeError: 'module' object has no attribute 'update'
'''},
{'date': 'Sun Mar 10 2024 11:46:55.308 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 15
    cena = Cena("/_ativo/jardim/mirante.jpg").vai()
  module _spy.vitollino.main line 1098
    self._cria_divs(width)
  module _spy.vitollino.main line 1103
    divesq.style.width = width // 3  # 100
TypeError: unsupported operand type(s) for //: 'str' and 'int'
'''},
{'date': 'Sun Mar 10 2024 11:49:25.282 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 15
    cena = Cena("https://activufrj.nce.ufrj.br/studio/labase/mirante.jpg?disp=inline&size=G").vai()
  module _spy.vitollino.main line 1098
    self._cria_divs(width)
  module _spy.vitollino.main line 1103
    divesq.style.width = width // 3  # 100
TypeError: unsupported operand type(s) for //: 'str' and 'int'
'''},