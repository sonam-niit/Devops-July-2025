provider "vault"{
    # address = "http://127.0.0.1:8200"
    # token = var.VAULT_TOKEN # detect automatically
}

data "vault_kv_secret" "db" {
  path = "secret/db-pass"
}

