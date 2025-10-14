{ pkgs ? import <nixpkgs> { } }:

let
  python = pkgs.python312; # или pkgs.python313
  pythonEnv = python.withPackages
    (ps: with ps; [ django whitenoise brotli gunicorn psycopg2 ]);
in pkgs.mkShell {
  buildInputs = [
    pythonEnv
    # pkgs.postgresql # если нужна локальная БД
  ];

  shellHook = ''
    echo "Django development environment loaded"
    # echo "Python version: $(python --version)"
  '';
}

