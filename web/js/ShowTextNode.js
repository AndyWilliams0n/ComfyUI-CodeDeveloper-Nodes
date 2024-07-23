import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

app.registerExtension({
  name: "Comfy.ShowTextNode",

  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === "CodeDeveloper_Display_Text") {

      // Node onCreated

      const onNodeCreated = nodeType.prototype.onNodeCreated;

      nodeType.prototype.onNodeCreated = function () {
        const node = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;

        let showTextNode = app.graph._nodes.filter((wi) => wi.type == nodeData.name),
        nodeName = `${nodeData.name}_${showTextNode.length}`;

        // LOG
        console.log(`CREATED NODE: ${nodeData.name}: ${nodeName}`);

        const wi = ComfyWidgets.STRING(
          this,
          nodeName,
          [
            "STRING",
            {
              default: "",
              placeholder: "Text will be shown here",
              multiline: true,
            },
          ],
          app
        );
        
        wi.widget.inputEl.readOnly = true;

        return node;
      };

      
      // Output Function

      const outSet = function (texts) {
        if (texts.length > 0) {
          if (Array.isArray(texts)) {
            texts = texts
              .filter((word) => word.trim() !== "")
              .map((word) => word.trim())
              .join(" ");
          }

          this.widgets[(this?.widgets.findIndex(
            (w) => w.type == "customtext"
          ))].value = texts;

          app.graph.setDirtyCanvas(true);

          // LOG
          console.log(`NODE OUTPUT: ${texts}`);
        }
      };


      // Node onExecuted

      const onExecuted = nodeType.prototype.onExecuted;

      nodeType.prototype.onExecuted = function (texts) {
        onExecuted?.apply(this, arguments);

        outSet.call(this, texts?.string);
      };
      

      // Node onConfigure
      const onConfigure = nodeType.prototype.onConfigure;
      
      nodeType.prototype.onConfigure = function (w) {
        onConfigure?.apply(this, arguments);
      
        if (w?.widgets_values?.length) {
          outSet.call(this, w.widgets_values);
        }
      };
    }
  },
});