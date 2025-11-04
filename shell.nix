{ pkgs ? import <nixpkgs> { } }:

let
  python = pkgs.python312;
  pythonEnv = python.withPackages
    (ps: with ps; [ django whitenoise brotli gunicorn psycopg2 ]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];

  shellHook = ''
    echo "Django development environment loaded"
    echo "Python version: $(python --version)"
  '';
}

