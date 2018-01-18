FROM python
WORKDIR /usr/src/app
COPY . .
RUN  bash installDeps.sh
ENTRYPOINT ["python", "src/coinPicker.py"]
