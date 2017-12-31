FROM myanaconda

WORKDIR /etc
RUN echo "backend : Agg" >> matplotlibrc

WORKDIR /usr/src/app
CMD [ "python", "./index.py" ]
