FROM <-mk_init_odoo_image->:<-mk_init_odoo_version->

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip debugpy

USER odoo