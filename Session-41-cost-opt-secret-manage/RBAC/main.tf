# role creation
resource "kubernetes_role" "pod_reader" {
  metadata {
    name = "pod-reader"
    namespace = "dev"
  }
  rule {
    api_groups = [""]
    resources = ["pods"]
    verbs = ["get","list"]
  }
}

resource "kubernetes_role_binding" "dev_user_binding" {
  metadata {
    name = "pod-reader-binding"
    namespace = "dev"
  }
  subject {
    kind = "User"
    name="dev-user"
    api_group = "rbac.authorization.k8s.io"
  }
  role_ref {
    kind = "Role"
    name = kubernetes_role.pod_reader.metadata[0].name
    api_group = "rbac.authorization.k8s.io"
  }
}