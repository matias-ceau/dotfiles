(setf (uiop/os:getenv "WEBKIT_DISABLE_COMPOSITING_MODE") "1")

;; buffer instead of web-buffer
(define-configuration web-buffer
  ((default-modes
    (pushnew 'nyxt/mode/vi:vi-normal-mode %slot-value%))))

;; (define-configuration browser
;;   ((theme (make-instance 'theme:theme 
;;                          :dark-p t
;; 			 :background-color- "#1C1B1A"
;; 			 :background-color "#100F0F"
;; 			 :background-color+ "#282726"
;; 			 :on-background-color "#CECDC3"
;; 			 :primary-color- "#878580"
;; 			 :primary-color "#6F6E69"
;; 			 :primary-color+ "#575653"
;; 			 :on-primary-color "#FFFCF0"
;; 			 :secondary-color- "#403E3C"
;; 			 :secondary-color "#343331"
;; 			 :secondary-color+ "#282726"
;; 			 :on-secondary-color "#CECDC3"
;; 			 :action-color- "#8B7EC8"
;; 			 :action-color "#AD8301"
;; 			 :action-color+ "#D0A215"
;; 			 :on-action-color "#100F0F"
;; 			 :highlight-color- "#DA702C"
;; 			 :highlight-color "#D0A215"
;; 			 :highlight-color+ "#FCEEB8"
;; 			 :on-highlight-color "#100F0F"
;; 			 :success-color- "#66800B"
;; 			 :success-color "#879A39"
;; 			 :success-color+ "#DAD8CE"
;; 			 :on-success-color "#100F0F"
;; 			 :warning-color- "#BC5215"
;; 			 :warning-color "#DA702C"
;; 			 :warning-color+ "#FCEEB8"
;; 			 :on-warning-color "#100F0F"
;; 			 :codeblock-color- "#1C1B1A"
;; 			 :codeblock-color "#282726"
;; 			 :codeblock-color+ "#343331"
;; 			 :on-codeblock-color "#CECDC3"
;; 			 :text-color- "#DAD8CE"
;; 			 :text-color "#CECDC3"
;; 			 :text-color+ "#B7B5AC"
;; 			 :contrast-text-color "#100F0F"
;;   ))))
;;

(define-configuration browser
 ((theme (make-instance 'theme:theme 
                        :dark-p t
                        :background-color- "#000000"  ; true_black
                        :background-color "#100F0F"   ; black (bg)
                        :background-color+ "#1C1B1A"  ; brblack (bg-2)
                        :on-background-color "#CECDC3" ; brwhite (tx)
                        :primary-color- "#878580"     ; base-500
                        :primary-color "#6F6E69"      ; base-600
                        :primary-color+ "#575653"     ; base-700
                        :on-primary-color "#FFFFFF"   ; true_white
                        :secondary-color- "#403E3C"   ; base-800
                        :secondary-color "#343331"    ; base-850
                        :secondary-color+ "#282726"   ; base-900
                        :on-secondary-color "#CECDC3" ; brwhite (tx)
                        :action-color- "#3AA99F"      ; brcyan
                        :action-color "#AD8301"       ; yellow
                        :action-color+ "#CE5D97"      ; brmagenta
                        :on-action-color "#100F0F"    ; black (bg)
                        :highlight-color- "#DA702C"   ; brorange
                        :highlight-color "#D0A215"    ; bryellow
                        :highlight-color+ "#FCEEB8"   ; yellow-100
                        :on-highlight-color "#100F0F" ; black (bg)
                        :success-color- "#66800B"     ; green
                        :success-color "#879A39"      ; brgreen
                        :success-color+ "#DAD8CE"     ; base-100
                        :on-success-color "#100F0F"   ; black (bg)
                        :warning-color- "#AF3029"     ; red
                        :warning-color "#D14D41"      ; brred
                        :warning-color+ "#DA702C"     ; brorange
                        :on-warning-color "#100F0F"   ; black (bg)
                        :codeblock-color- "#1C1B1A"   ; brblack (bg-2)
                        :codeblock-color "#282726"    ; base-900
                        :codeblock-color+ "#343331"   ; base-850
                        :on-codeblock-color "#CECDC3" ; brwhite (tx)
                        :text-color- "#DAD8CE"        ; base-100
                        :text-color "#CECDC3"         ; brwhite (tx)
                        :text-color+ "#B7B5AC"        ; base-200
                        :contrast-text-color "#100F0F" ; black (bg)
 ))))


(defvar *my-search-engines*
  (list
   '("google" "https://google.com/search?q=~a" "https://google.com")
   '("python3" "https://docs.python.org/3/search.html?q=~a"
     "https://docs.python.org/3")
   '("doi" "https://dx.doi.org/~a" "https://dx.doi.org/"))
  "List of search engines.")

(define-configuration context-buffer
  "Go through the search engines above and `make-search-engine' out of them."
  ((search-engines
    (append
     (mapcar (lambda (engine) (apply 'make-search-engine engine))
             *my-search-engines*)
     %slot-default%))))

(defmethod initialize-instance :after
           ((interface password:keepassxc-interface)
            &key &allow-other-keys)
  "It's obviously not recommended to set master password here,
as your config is likely unencrypted and can reveal your password to someone
peeking at the screen."
  (setf (password:password-file interface)
          "/home/matias/.localdata/monkeypass/database.kdbx"
        (password:key-file interface) "/home/matias/notes/resources/georgeabitbol"
	(password:yubikey-slot interface) nil
        ))

(define-configuration nyxt/mode/password:password-mode
  ((nyxt/mode/password:password-interface
    (make-instance 'password:keepassxc-interface))))

(define-configuration buffer
  ((default-modes
    (append (list 'nyxt/mode/password:password-mode) %slot-value%))))


;; (define-configuration web-buffer
;;   ((default-modes
;;     (pushnew 'nyxt/mode/blocker:blocker-mode %slot-value%))))

