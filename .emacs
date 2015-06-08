;; Hello Madgrid 
;; Becarefull with my DNA code!
(require 'package)
(require 'json)
(add-to-list 'package-archives '("melpa" . "http://melpa.milkbox.net/packages/") t)
(add-to-list 'package-archives '("marmalade" . "http://marmalade-repo.org/packages/"))

;; Please set your themes directory to 'custom-theme-load-path
(add-to-list 'custom-theme-load-path
             (file-name-as-directory "~/.emacs.d/custom_themes/"))

;; Initialize package mode along with all the installed packages
(package-initialize)

;; Enable Projectile globally
(projectile-global-mode)
(setq projectile-completion-system 'helm)
(helm-projectile-on)
(global-set-key (kbd "C-c h") 'helm-projectile)


;; Python IDE http://onthecode.com/post/78817537628/emacs-on-steroids-for-python-elpy-el
(require 'elpy)
(elpy-enable)
;; Fixing a key binding bug in elpy
(define-key yas-minor-mode-map (kbd "C-c k") 'yas-expand)
;; Fixing another key binding bug in iedit mode
(define-key global-map (kbd "C-c o") 'iedit-mode)
;; PYTHONPATH environmental variable
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(elpy-interactive-python-command "python3")
 '(elpy-rpc-python-command "python3")
 '(elpy-use-cpython "python3")
 '(python-shell-interpreter "python3"))



;; Load your favorite theme
(load-theme 'dark-krystal t t)
(enable-theme 'dark-krystal)
;;(load-theme 'green-phosphor t t)
;;(enable-theme 'green-phosphor)

;; Enable Evil
(require 'evil)
(evil-mode 1)

;; Line Number
(global-linum-mode t)

;; Transparent Background
(set-frame-parameter (selected-frame) 'alpha '(85 85))
(add-to-list 'default-frame-alist '(alpha 85 85))
